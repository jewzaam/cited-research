# Async, Threading, and C# .NET 8 Style

Dimension covers: UI dispatcher patterns, `async void` vs `async Task`, CancellationToken propagation, NINA exception handling, .NET 8 language features (nullable, file-scoped namespaces, primary constructors, records).

See [citations](../citations.md).

## UI dispatcher pattern

WPF rule: anything that touches a UI-bound property or visual must run on the UI thread. NINA's mediator events ([mediators-and-devices](mediators-and-devices.md)) may fire on a background thread — assume so unless proved otherwise. The modern WPF idiom [48]:

```csharp
await Application.Current.Dispatcher.InvokeAsync(() => {
    SomeUIBoundProperty = newValue;
});
```

Avoid `Dispatcher.BeginInvoke(...)` — it is the legacy fire-and-forget form and does not integrate with `async/await` [48]. Use `InvokeAsync` because it returns a `DispatcherOperation` whose `.Task` integrates with the async chain and surfaces exceptions to the awaiter.

For NINA's `IImageSaveMediator.BeforeImageSaved` and `BeforeFinalizeImageSaved` events [13] (delegate type `Func<object, T, Task>`), the publisher already `await`s the handler — those handlers must return `Task` and use `async Task` cleanly. The fire-and-forget `EventHandler<ImageSavedEventArgs>` on `ImageSaved` [13] is the case where `async void` is the only delegate-compatible option.

## `async void` rules in NINA plugin code

Per [48]:

| When | Use | Why |
|---|---|---|
| Subscribing to an `EventHandler` or `EventHandler<T>` (sync delegate) on a NINA mediator | `async void` (top-level handler only) | Delegate signature returns void; nothing else fits |
| Subscribing to a `Func<..., Task>` event (`BeforeImageSaved`) | `async Task` | Publisher awaits returned task |
| Any other method | `async Task` | Lets caller await/observe |

Critical rule [48]: every `async void` handler body must be wrapped in `try { ... } catch (Exception ex) { Logger.Error(ex); }`. An unhandled exception from `async void` propagates to the captured `SynchronizationContext` and **can crash NINA** because the host has not been observed to wire a global `DispatcherUnhandledException` handler that suppresses plugin exceptions.

## CancellationToken propagation

Per [54]:
- `CancellationToken` is the **last parameter** of every async method, unless followed by `IProgress<T>` (in which case CancellationToken precedes Progress per NINA's convention; see `IImagingMediator.CaptureImage(...)` [12]).
- Pass the token through every layer; do not introduce new tokens unless you need composition (`CancellationTokenSource.CreateLinkedTokenSource(...)`).
- Inside `Task.Run(() => ..., cancellationToken)` always pass the token to BOTH `Task.Run` and the inner work — `Task.Run` honours it only for queue-time cancellation.
- Sequencer instructions receive a `CancellationToken` representing user-stop; forwarding it through every `HttpClient.SendAsync(..., ct)`, `Stream.ReadAsync(..., ct)`, etc. is required for sequence-stop to feel responsive.
- `CancellationToken.ThrowIfCancellationRequested()` only at boundaries where no inner async call would already surface the cancellation; over-use creates noise stack frames.

Common plugin mistake: `Task.Run(() => SomeWork())` with no token — sequence-stop does nothing for that work.

## NINA exception swallowing

`PluginLoader.cs` [7] catches `ReflectionTypeLoadException` and synthesizes a fallback manifest on failure to load. Sequencer instruction failures are scoped (sequencer marks the instruction failed, continues or aborts per user config). For mediator events and direct callbacks, NINA's handler-iteration code was not fully inspected; **a defensive plugin assumes mediator events do not swallow handler exceptions**. Always wrap your handler bodies; never `throw` from an event handler in a way that escapes the plugin boundary.

## .NET 8 nullable annotations

WPF framework APIs lack full nullable annotations as of .NET 8 [49]. Enabling `<Nullable>enable</Nullable>` project-wide in a NINA plugin produces warnings against:
- `IValueConverter.Convert(...)` (declared `object` but conceptually nullable)
- ICommand parameters
- XAML code-behind generated `partial` classes

Pragmatic policy: enable nullable project-wide for plugin business code, then `#nullable disable` per-file in XAML code-behind and converter files. NINA's own source (NINA.Core targeting `net10.0-windows` on develop [11]) does not enable nullable globally — partial per-file enablement is the realistic precedent.

`NINA.Plugin` NuGet assemblies are not annotated, so injected mediator references are typed `IFooMediator` rather than `IFooMediator?`. Treat them as non-null after `[ImportingConstructor]` injection (MEF will not call the constructor without resolving every import).

## File-scoped namespaces (C# 10)

`namespace Foo.Bar;` instead of the block form. Constraints [50]:
- Exactly one file-scoped namespace per file
- Cannot mix with block-scoped namespaces in the same file
- `using` directives appear before the namespace declaration

The plugin template [2] uses the block form because it dates from older .NET. New plugin code can adopt file-scoped namespaces freely — they compile identically and reduce indent. Set `csharp_style_namespace_declarations = file_scoped` in `.editorconfig` to enforce.

## Primary constructors (C# 12)

Per [51], [52]: primary constructor parameters scope across the entire class body. Attributes on the synthesized constructor use the `method:` target:

```csharp
[Export(typeof(IPluginManifest))]
public class MyPlugin(IProfileService profileService, IImageSaveMediator imageSaveMediator)
    : PluginBase {
    // Body uses profileService, imageSaveMediator directly
}
```

To mark the synthesized constructor as the MEF importing constructor:

```csharp
[method: ImportingConstructor]
public class MyPlugin(IProfileService profileService) : PluginBase {
    // ...
}
```

Per [53], MEF requires at most one `[ImportingConstructor]` per class — the primary constructor satisfies this. **Caveat:** per-parameter `[Import(AllowDefault = true, ContractName = "...")]` annotations on primary-constructor parameters are not supported [51]. If you need per-parameter import customization (rare in NINA plugins), fall back to an explicit constructor.

Observed reality: no inspected NINA plugin currently uses primary constructors for `[Export(typeof(IPluginManifest))]` classes — they all use explicit `[ImportingConstructor]` constructors with conventional bodies [2], [27], [31]. The pattern works in theory but is unproven in production NINA plugins.

The `[ObservableProperty]` source generator [43] requires `partial class`. Primary constructors are orthogonal — `partial class Foo(IBar bar)` is legal.

## Records and other features

- `record` types do not implement `INotifyPropertyChanged` and are unsuitable for mutable VM properties used in two-way WPF bindings. Use for immutable DTOs and mediator-message payloads only.
- `record struct` works for small value objects in hot paths.
- Pattern matching, switch expressions, collection expressions — no WPF/NINA-specific gotchas, use freely.
- `using` declarations (`using var x = ...;`) dispose at end of scope [55]; prefer them for single-disposable methods. Use the block form when explicit early disposal matters (e.g., releasing a lock before a long async wait).
- Top-level statements — irrelevant for class libraries.

## Recommended style for new NINA plugins

```csharp
// Foo/MyPlugin.cs
using NINA.Plugin;
using NINA.Plugin.Interfaces;
using NINA.Profile.Interfaces;

namespace MyOrg.MyPlugin;     // file-scoped namespace

[Export(typeof(IPluginManifest))]
public class MyPlugin : PluginBase, INotifyPropertyChanged {
    private readonly IProfileService profileService;

    [ImportingConstructor]
    public MyPlugin(IProfileService profileService) {
        this.profileService = profileService;
        // subscribe events here
    }

    public override async Task Teardown() {
        // unsubscribe events here
        await base.Teardown();
    }

    public event PropertyChangedEventHandler? PropertyChanged;
    protected void RaisePropertyChanged([CallerMemberName] string? name = null)
        => PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(name));
}
```

Rationale: file-scoped namespace, explicit `[ImportingConstructor]` (matches all real plugins), explicit `INotifyPropertyChanged` with `[CallerMemberName]` (matches template [2]), nullable annotations on the event/handler signature.

## Gaps and limitations

- The thread on which each specific NINA mediator event fires is not source-verified; the dispatcher-marshalling guidance is conservative.
- The recommendation against primary constructors for `[Export]` classes is based on absence of evidence in real plugins, not on a documented incompatibility. The pattern should work; using it makes the plugin a slight outlier.
- Whether NINA's mediator-event publisher catches handler exceptions or lets them propagate is not directly confirmed from fetched source.
