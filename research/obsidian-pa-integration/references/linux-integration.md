# Linux Desktop Integration

## Dimension Coverage

This reference covers Obsidian's Linux support — packaging formats, Wayland/X11 compatibility, and `obsidian://` protocol handler registration.

For source details, see [citations.md](../citations.md).

## Package Formats

Obsidian is available on Linux in multiple formats:

| Format | Source | Notes |
|---|---|---|
| AppImage | obsidian.md/download | Historically the "official" format; ARM64 available [1] |
| Flatpak | Flathub (verified) | `md.obsidian.Obsidian`; verified publisher status |
| Snap | Snap Store | `sudo snap install obsidian --classic` |
| .deb | obsidian.md/download | Available for Debian/Ubuntu-based systems |

Obsidian is an Electron-based application [35].

### Packaging Trade-offs for PA Integration

| Format | PA file access | CLI compatibility | URI handler |
|---|---|---|---|
| AppImage | Direct filesystem | Symlink at `/usr/local/bin/obsidian` [1] | Requires manual .desktop file [18] |
| Flatpak | Sandbox restrictions | May need Flatpak exec wrapper | Requires permission overrides |
| Snap | `--classic` flag provides full access | Special considerations noted [1] | Depends on snap confinement |
| .deb | Direct filesystem | Native binary | Standard .desktop integration |

**Recommendation for PA integration:** AppImage or .deb provide the most straightforward filesystem access for a PA writing directly to vault files. Flatpak's sandbox and Snap's confinement add complexity [17].

## Wayland / X11 Support

Obsidian runs on both Wayland and X11 as an Electron application [35].

- Flatpak requires Wayland socket override: `flatpak override --user --socket=wayland md.obsidian.Obsidian` [35]
- Wayland benefits: fractional scaling, multi-touch gestures, window sizing retention [35]
- Common issue: blurry display without Wayland configuration [35]
- XWayland compatibility available as fallback [35]

## URI Protocol Handler Setup

On Linux, the `obsidian://` URI scheme requires manual configuration [4][18].

### Prerequisites

```bash
sudo apt install xdg-utils desktop-file-utils
```
[18]

### .desktop File

Create `~/.local/share/applications/obsidian.desktop` [18]:

```ini
[Desktop Entry]
Name=Obsidian
Exec=/path/to/Obsidian.AppImage %u
Terminal=false
Type=Application
Icon=/path/to/icon.png
StartupWMClass=obsidian
Comment=Obsidian
Categories=Office;
MimeType=text/html;x-scheme-handler/obsidian;
```

**Critical:** The `%u` parameter in the Exec line is required to pass URIs [18]. Use full paths, not tilde [18]. No trailing whitespace on any line [18].

### Registration

```bash
update-desktop-database ~/.local/share/applications/
```
[18]

### Testing

```bash
xdg-open "obsidian://new?vault=notes&name=note&content=content"
```
[18]

### Known Issues

- Chrome may not handle `obsidian://` URIs on Linux; Firefox works [18]
- AppImage's bundled `.desktop` file historically lacked the `%u` parameter [37]
- System-wide setup uses `/usr/local/share/applications/` with sudo [18]

## PA Integration Assessment

**Built-in vs plugin:** Linux support is built-in. URI handler setup is a manual OS-level configuration, not a plugin.

**Requires Obsidian running:** For URI schemes and CLI, yes. For direct file access to vault, no.

**Works against files on disk:** Yes — vault files are accessible at their filesystem paths regardless of Obsidian's state.

## Gaps and Limitations

- Which package format receives updates fastest is not documented
- Flatpak sandbox restrictions for vault access not fully documented
- Wayland support may vary by desktop environment (GNOME, KDE, etc.) [35]
- No official PPA for automatic .deb updates documented
