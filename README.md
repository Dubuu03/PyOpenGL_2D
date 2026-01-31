# PyOpenGL_2D

Simple renderer that draws text-defined pixel art using PyOpenGL + Pygame with instanced rendering.

Requirements
- Python 3.8+
- pygame, PyOpenGL, numpy

Install
```bash
pip install pygame PyOpenGL numpy
```

Run
```bash
python main.py
```

Quick notes
- Edit display/grid in `config.py` (DISPLAY_WIDTH, DISPLAY_HEIGHT, GRID_SIZE).
- `pixel_map.txt`: space-separated tokens per row; lines starting with `#` or blank are ignored.
- Colors are defined in `texture_loader.py` (COLOR_MAP).
- Core files:
  - `main.py` — init, buffers, render loop
  - `shader.py` — vertex/fragment shaders + compilation
  - `pixel.py` — quad VAO/VBO/EBO creation
  - `texture_loader.py` — loads map -> color array

License
- No license included. Add a LICENSE file if you want to publish or share.
