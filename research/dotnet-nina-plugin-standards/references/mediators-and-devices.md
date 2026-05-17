# Mediators and Device Consumers

Dimension covers: `I*Mediator` event subscription, `IDeviceConsumer<T>` registration via `IDeviceMediator<,,>`, thread semantics, cleanup.

See [citations](../citations.md).

## Two distinct interaction patterns

NINA's mediator surface uses **two different idioms** depending on what you want:

1. **Event subscription** (`event +=` / `-=`) — for discrete actions like "image was saved" or "telescope was parked".
2. **Consumer registration** (`mediator.RegisterConsumer(this)` / `mediator.RemoveConsumer(this)`) — for streaming device-state polling updates delivered via the `IDeviceConsumer<TInfo>.UpdateDeviceInfo(TInfo)` callback.

Both patterns coexist. A plugin can register as a `ITelescopeConsumer` to receive position/tracking-state polls *and* subscribe to `Slewed` events on `ITelescopeMediator` [14].

## Generic IDeviceMediator pattern

Per [15], the contract is:

```csharp
public interface IDeviceMediator<THandler, TConsumer, TInfo>
    where THandler : IDeviceVM<TInfo>
    where TConsumer : IDeviceConsumer<TInfo>
{
    void RegisterConsumer(TConsumer consumer);
    void RemoveConsumer(TConsumer consumer);   // note: Remove, not Unregister
    void Broadcast(TInfo deviceInfo);
    // ... device-specific methods
}
```

Concrete device mediators specialize this — `ITelescopeMediator : IDeviceMediator<ITelescopeVM, ITelescopeConsumer, TelescopeInfo>` [14] — and add device-specific methods + events.

Consumers implement `IDeviceConsumer<TInfo>` (e.g., `ITelescopeConsumer : IDeviceConsumer<TelescopeInfo>`) which carries `void UpdateDeviceInfo(TInfo info)`.

## Per-device events (NINA 3.x)

Per [57]: "Device mediators have been enhanced with numerous new events that subscribers can monitor following an action performed by the device (e.g., mount slewing, cover opening, etc.)."

Confirmed events from [14]:

| Mediator | Events |
|---|---|
| `ITelescopeMediator` | `BeforeMeridianFlip`, `AfterMeridianFlip`, `Parked`, `Homed`, `Unparked`, `Slewed` |

Other per-device mediators (`ICameraMediator`, `IFocuserMediator`, `IFilterWheelMediator`, `IGuiderMediator`, `IRotatorMediator`, `IDomeMediator`, `IFlatDeviceMediator`, `ISafetyMonitorMediator`, `IWeatherDataMediator`, `ISwitchMediator`) follow the same pattern but their exact event lists were not fully fetched. Treat the per-device event surface as authoritative-on-inspection.

## Image-pipeline events live on IImageSaveMediator, not IImagingMediator

A common confusion: `IImagingMediator` [12] does **not** expose an `ImageSaved` event. Its only event is `ImagePrepared` (carrying `ImagePreparedEventArgs { IRenderedImage RenderedImage; PrepareImageParameters Parameters; }`).

The save-pipeline events are on `IImageSaveMediator` [13]:

| Event | Delegate type | Timing |
|---|---|---|
| `BeforeImageSaved` | `Func<object, BeforeImageSavedEventArgs, Task>` | Before save, before full processing |
| `BeforeFinalizeImageSaved` | `Func<object, BeforeFinalizeImageSavedEventArgs, Task>` | After processing, before final destination move |
| `ImageSaved` | `EventHandler<ImageSavedEventArgs>` | After persistence |

The two `Func<..., Task>` events use the **async-event idiom**: subscribers may `await` work inside handlers and the publisher awaits the returned `Task`. This is how the template plugin [2] inserts FITS headers and image patterns. Regular `EventHandler<ImageSavedEventArgs>` (`ImageSaved`) is fire-and-forget — handlers should not throw and should be quick or queue work to a background task.

Per [13] source comment on `BeforeFinalizeImageSaved`: "Altering Image Meta Data will NOT be reflected in the written file." Use `BeforeImageSaved` to mutate FITS keywords.

`IImageSaveMediator.Enqueue(IImageData, Task<IRenderedImage>, IProgress<ApplicationStatus>, CancellationToken)` [13] is the producer side — plugins that generate their own images push them into the pipeline through this method.

## Thread semantics

NINA is a WPF application built on .NET 8/10; it has a UI dispatcher [11]. The mediator implementations were not fetched in full, so we do not have ground-truth confirmation of which thread each event fires on. **Conservative rule documented across the C# / WPF community [48]:**

- Treat all mediator events as potentially firing on a background thread.
- If the handler updates UI-bound properties or interacts with WPF controls, marshal to UI via `await Application.Current.Dispatcher.InvokeAsync(...)`.
- Do not use `Dispatcher.BeginInvoke` in modern code — it does not integrate with `async/await` [48].

`UpdateDeviceInfo(TInfo)` is invoked from NINA's hardware-poll timer; treat it as background-thread by default and dispatch UI work explicitly.

## Cleanup contract

Every event subscription and consumer registration must be reversed in `Teardown()` [9]. The template [2] is the canonical example:

```csharp
public override Task Teardown() {
    profileService.ProfileChanged -= ProfileService_ProfileChanged;
    imageSaveMediator.BeforeImageSaved -= ImageSaveMediator_BeforeImageSaved;
    imageSaveMediator.BeforeFinalizeImageSaved -= ImageSaveMediator_BeforeFinalizeImageSaved;
    return base.Teardown();
}
```

The InfluxDB exporter [27] adds consumer registration cleanup symmetrically.

`PluginBase` does not implement `IDisposable` [8], so `Teardown()` is the only documented cleanup hook. Plugins that need deterministic disposal of background work should also store a `CancellationTokenSource` in a field, call `Cancel()` in `Teardown()`, then dispose [27].

## Pitfalls

1. **Anonymous lambda subscriptions** cannot be unsubscribed — the `-=` operator only removes equal delegate instances. Always use a named method or capture the lambda in a field. Confirmed pattern in [2].
2. **Capturing `this` in long-lived handlers** holds the plugin instance alive; failing to unsubscribe in `Teardown()` is a classic strong-reference event leak.
3. **`async void` handler exceptions** propagate to the UI `SynchronizationContext` and can crash NINA [48]. Wrap every async-void handler body in `try / catch { Logger.Error(ex); }`.
4. **`UpdateDeviceInfo` on UI thread** would block hardware polling. Don't `await Dispatcher.InvokeAsync(...)` synchronously inside it without considering throttling.
5. **`ISequenceMediator` early access** — per [1], must not be touched in `[ImportingConstructor]`; defer until after all plugins are loaded (e.g. in `Initialize()`).

## Gaps and limitations

- The exact `IDeviceConsumer.cs` file location in NINA source was not fetched (404 on the path attempted). The contract is reverse-engineered from `IDeviceMediator.cs` [15]: a single generic method `UpdateDeviceInfo(TInfo info)`.
- Per-event thread origin for each mediator's events is not source-confirmed; the dispatcher-marshalling guidance above is conservative.
- `RegisterConsumer` weak-vs-strong reference semantics — the source notes `RemoveConsumer` is a named method, implying strong references that must be removed explicitly.
