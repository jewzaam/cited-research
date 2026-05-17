# Testing NINA Plugins

Dimension covers: test framework choice, mocking, `[ObservableProperty]` source-generator interaction, `[InternalsVisibleTo]`, TFM, WPF/Dispatcher in tests.

See [citations](../citations.md).

## Evidence gap

No comprehensive test project was discovered in any of the surveyed plugin repositories (`isbeorn/nina.plugin.template`, `daleghent/nina-influxdb-exporter`, `christian-photo/ninaAPI`, `ghilios/joko.nina.plugins`, `tcpalmer/nina-scheduler`). Search results returned the repo READMEs and source files but no `*.Tests.csproj` or `tests/` directory was surfaced. The plugin template [1] does not include a test scaffold.

This means the NINA plugin ecosystem **has no published convention for unit testing plugins**. The recommendations below are derived from NINA core's own test conventions [42] and general .NET 8 testing best practice.

## NINA core convention: NUnit + FluentAssertions

Per NINA's `CONTRIBUTING.md` [42]:

> "The NINA project uses the NUnit unit-testing framework to write and run automated unit tests, and additionally uses Fluent Assertions to write easy to read assertions."

Test run command:
```
dotnet test NINA.Test/NINA.Test.csproj --configuration Debug --no-build -p:PlatformTarget=x64
```

NINA core uses NUnit. Plugin authors who want to match NINA's style should use NUnit + FluentAssertions; plugin authors who want broader .NET ecosystem familiarity can reasonably choose xUnit. There is no NINA-imposed constraint either way for plugins.

## Recommendation

For new plugin development:

| Tool | Recommended | Alternative |
|---|---|---|
| Test framework | xUnit (broader .NET tooling support, faster Visual Studio test explorer) | NUnit (matches NINA core [42]) |
| Mock library | Moq | NSubstitute |
| Assertions | FluentAssertions (matches NINA core [42]) | Built-in xUnit/NUnit |
| WPF/STA helper | `Xunit.StaFact` (`[WpfFact]`, `[StaFact]`, `[UIFact]`) [46] | Manually marshal SynchronizationContext |

xUnit + Moq + FluentAssertions is the most common .NET 8 stack in 2026 and works cleanly with C# 12 features.

## Target framework for the test project

Two paths [47]:

1. **Test project targets `net8.0-windows`** (matches plugin). Required if tests touch WPF types directly (controls, Dispatcher, ObservableCollection updates from non-UI threads). Pin to `net8.0-windows10.0.22621.0` to avoid the NUnit `net8.0-windows` + `win-x64` RID incompatibility [47].

2. **Test project targets `net8.0`** (pure .NET). Cannot reference the plugin's `net8.0-windows` assembly directly. Requires extracting non-UI logic (data converters, manifest readers, business rules) into a `net8.0`-targeting library project that both the plugin and the test project reference.

The second path is preferred when feasible because non-Windows test runners (CI containers, Linux dev machines) can execute it. Aim to keep WPF code thin (XAML + minimal code-behind), all logic in `net8.0` libs, tested without WPF dependencies.

## Mocking NINA mediators

The mediator interfaces (`IImagingMediator` [12], `ITelescopeMediator` [14], `IImageSaveMediator` [13], etc.) are pure interfaces with no abstract base class or non-virtual members blocking mocking:

```csharp
var imagingMock = new Mock<IImagingMediator>();
imagingMock.Setup(m => m.CaptureImage(It.IsAny<CaptureSequence>(),
                                       It.IsAny<CancellationToken>(),
                                       It.IsAny<IProgress<ApplicationStatus>>(),
                                       It.IsAny<string>()))
           .Returns(Task.FromResult<IExposureData>(null));
```

Events on interfaces can be raised through `Mock.Raise(...)`:

```csharp
imagingMock.Raise(m => m.ImagePrepared += null, new ImagePreparedEventArgs { ... });
```

`IImageSaveMediator.BeforeImageSaved` is typed `Func<object, BeforeImageSavedEventArgs, Task>` [13] — raising it from a mock requires `imageSaveMock.Raise(m => m.BeforeImageSaved += null, sender, args)` (Moq supports this since v4.x).

`IProfileService` [19] and `IPluginOptionsAccessor` [16] are also pure interfaces and mockable cleanly.

## `[ObservableProperty]` source generator in tests

Per [43]: the generator emits standard `public` properties on a `partial` class. They are **not** `virtual`, so Moq cannot proxy them on concrete classes. Strategy:

| Goal | Approach |
|---|---|
| Verify a VM raises PropertyChanged | Instantiate the real VM; subscribe to `PropertyChanged`; assert the event fires on set |
| Substitute a VM in a test | Define an interface for the VM and inject the interface, not the concrete class — then Moq the interface |
| Test the `OnPropertyNameChanged` partial hook | Instantiate real VM; spy on the side effect |

`INotifyPropertyChanged` events from `[ObservableProperty]` fire **synchronously on the calling thread** — no Dispatcher needed. Tests can subscribe and assert without any STA / Dispatcher setup [43].

## `[InternalsVisibleTo]`

For tests that need to reach `internal` plugin types (private setters, internal helpers), add to the plugin's `.csproj`:

```xml
<ItemGroup>
  <InternalsVisibleTo Include="MyPlugin.Tests" />
</ItemGroup>
```

Per [45]: SDK-style csproj supports this directly. Unsigned NINA plugin assemblies (the norm) need only the assembly name; signed assemblies require the full public key.

This is helpful for plugins that have internal abstractions for testability but do not want them in the public plugin surface.

## WPF Dispatcher in tests

If a test exercises code that touches `Dispatcher.CurrentDispatcher` or `Application.Current.Dispatcher`, use `Xunit.StaFact` [46]:

```csharp
[WpfFact]
public void MyTest() {
    // Runs on STA thread with a real Dispatcher available
    var d = Application.Current?.Dispatcher;
    // ...
}
```

For tests that just need a `SynchronizationContext` (no STA), `SynchronizationContext.SetSynchronizationContext(new SynchronizationContext())` at the top of the test method suffices.

## Integration testing

No "load a plugin DLL into a NINA test host" integration framework exists in the NINA ecosystem at the time of writing. Plugins that need integration tests against real NINA build a test sequencer flow inside NINA manually.

## Pitfalls

1. **Targeting `net8.0` test against `net8.0-windows` plugin** — project reference is incompatible. Solution: extract logic into a `net8.0` lib.
2. **Mocking a concrete VM class with non-virtual `[ObservableProperty]` properties** — Moq cannot override; refactor to an interface or instantiate the real type.
3. **Raising an `async Task`-returning event from a Moq mock** — supported but requires Moq 4.x's `Raise` overloads that accept the args; older Moq versions can't.
4. **Forgetting `Xunit.StaFact` for Dispatcher-touching tests** — `Dispatcher.CurrentDispatcher` throws or returns null on the thread-pool threads xUnit uses by default.

## Gaps and limitations

- No real example of a NINA plugin test project to point readers at — recommendations are extrapolated.
- The exact NUnit `[Apartment(ApartmentState.STA)]` vs `Xunit.StaFact` trade-off is not validated against a real NINA plugin test.
- Whether NINA's own `NINA.Test.csproj` targets `net8.0-windows` or `net8.0` is not directly fetched.
