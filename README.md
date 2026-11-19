# MagicPhotos

A desktop photo editor in Python and PyQt5 (team university project, 2021): open a photo, then
add a background, frame, filter, shapes, text or a calendar page, and save it at a chosen size.

## Run

```sh
python3 -m venv .venv && . .venv/bin/activate      # Python 3.8 was used; Windows: .venv\Scripts\activate
pip install -r requiraments.txt                    # PyQt5, Pillow, OpenCV
python3 entrypoint.py
```

## What it can do

| Feature | Options |
|---|---|
| Background | colours from `editors/sources/backgrounds.json` |
| Frame | `frame1`, `frame2` (OpenCV borders) |
| Filter | black and white, sepia, brightness |
| Shapes | circles and stars: colour, position and size, or random (diamonds and hearts are listed in `FiguresEditor` but not implemented) |
| Text | text, colour, font (two bundled TTFs), size |
| Calendar | a month page next to the photo |
| Rotate | any angle |
| Save | 1000×1000, 700×700 or 600×400 |

## Layout

| Path | What |
|---|---|
| `entrypoint.py` | starts the Qt app |
| `gui/` | windows (main, figure, text, save): Qt Designer `.ui` files in `gui/src/`, generated renderers, handlers, combo-box options as JSON |
| `editors/base_editor.py` | `Editor` (a singleton): holds the image and applies every operation |
| `editors/figures_editor.py`, `filter_editor.py` | shapes and filters |
| `editors/sources/` | backgrounds, frames, texts, fonts, calendar and star images |
| `src/decorators.py` | the `@singleton` decorator |

The `gm_feature` branch is a teammate's development branch, kept for history.

Decisions: [docs/adr](docs/adr/README.md).
