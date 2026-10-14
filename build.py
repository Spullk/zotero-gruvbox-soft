#!/usr/bin/env python3
"""Package src/ into dist/gruvbox-soft.xpi and write dist/update.json.

Version comes from src/manifest.json, so to release: bump "version" there,
then push a matching git tag (e.g. v1.0.1). GitHub Actions runs this script
and publishes the release automatically.
"""
import json
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
DIST = ROOT / "dist"
REPO = "Spullk/zotero-gruvbox-soft"
XPI_NAME = "gruvbox-soft.xpi"

manifest = json.loads((SRC / "manifest.json").read_text())
version = manifest["version"]
zotero = manifest["applications"]["zotero"]

DIST.mkdir(exist_ok=True)

# Build the .xpi (just a zip with manifest.json at the root)
with zipfile.ZipFile(DIST / XPI_NAME, "w", zipfile.ZIP_DEFLATED) as zf:
    for path in sorted(SRC.rglob("*")):
        if path.is_file():
            zf.write(path, path.relative_to(SRC))

# update.json tells installed copies where the newest version lives
update = {
    "addons": {
        zotero["id"]: {
            "updates": [
                {
                    "version": version,
                    "update_link": f"https://github.com/{REPO}/releases/download/v{version}/{XPI_NAME}",
                    "applications": {
                        "zotero": {"strict_min_version": zotero["strict_min_version"]}
                    },
                }
            ]
        }
    }
}
(DIST / "update.json").write_text(json.dumps(update, indent=2) + "\n")

print(f"Built {XPI_NAME} v{version}")
