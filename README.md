# Gruvbox Soft for Zotero

A subtle, warm Gruvbox-dark theme for Zotero 7+. It only applies when Zotero's
**Appearance** is set to **Dark**, so Light mode stays stock.

## Install

1. Download `gruvbox-soft.xpi` from the [latest release](https://github.com/Spullk/zotero-gruvbox-soft/releases/latest).
2. In Zotero: **Tools → Plugins → ⚙ → Install Plugin From File…** and pick the `.xpi`.
3. **Settings → General → Appearance → Dark.**

Installed copies check this repo for updates and upgrade themselves automatically.

## Editing the theme

All colors live in [`src/style.css`](src/style.css). The palette is defined once at
the top as `--gb-*` variables, then mapped onto Zotero's own design tokens.

## Releasing a new version

1. Edit `src/style.css`.
2. Bump `"version"` in `src/manifest.json` (e.g. `1.0.0` → `1.0.1`).
3. Commit, then tag and push:
   ```bash
   git tag v1.0.1
   git push && git push --tags
   ```

GitHub Actions builds the `.xpi`, generates `update.json`, and publishes the
release. Every Zotero with the plugin installed picks it up on its next update check
(or immediately via **Tools → Plugins → ⚙ → Check for Updates**).

To build locally instead: `python3 build.py` → output in `dist/`.

## Palette

Colors from [Gruvbox](https://github.com/morhetz/gruvbox) by Pavel Pertsev (MIT).
