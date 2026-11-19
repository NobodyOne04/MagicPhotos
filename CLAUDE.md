# MagicPhotos

A 2021 team project: PyQt5 desktop photo editor (Pillow + OpenCV). Russian commit history.

## Commands
```sh
pip install -r requiraments.txt        # note the spelling; Python 3.8 era pins
python3 entrypoint.py
```
No tests.

## Layout
- `entrypoint.py`: Qt app start.
- `gui/<window>/`: generated renderer (`renderer.py` / `*_window.py`), `handlers.py`,
  `combo_boxes/*.json` (the options each dropdown shows); `gui/src/*.ui`: Qt Designer sources.
- `editors/`: `base_editor.Editor` (singleton, all image operations), `figures_editor`,
  `filter_editor`, `src/features.py` (random defaults), `sources/` (assets), `config.py` (paths).
- `docs/adr/`: decision records (`.adr`), index in `docs/adr/README.md`.

## Conventions
- Read the ADR before changing a recorded decision; commit subjects carry its number.
- Change a window in its `.ui` file and regenerate the Python (pyuic5); don't hand-edit both.
- A new dropdown option needs its JSON entry and the matching handler/editor code.
- `gm_feature` is a teammate's branch: don't delete it.
- Archived project: docs or small fixes only unless asked.
