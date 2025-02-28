import numpy as np

COLOR_MAP = {
    "A": (0.00, 0.00, 0.00),  # Background color
    "1": (0.00, 0.00, 0.00),  # Black
    "2": (0.19, 0.18, 0.18),  # Dark Gray
    "3": (0.57, 0.58, 0.62),  # Light Gray
    "Q": (1.00, 1.00, 1.00),  # White
    "W": (0.99, 0.37, 0.09),  #  Orange-Red
    "E": (1.00, 0.80, 0.01),  # Yellow
    "S": (0.99, 0.95, 0.61)   #  Cream
}

def load_pixel_art(filename, grid_size):
    rows, cols = grid_size  # Unpack grid size

    with open(filename, "r") as file:
        lines = file.readlines()

    pixel_colors = np.zeros((rows, cols, 3), dtype=np.float32)

    row = 0  # Track valid pixel rows
    for line in lines:
        line = line.strip()
        if line.startswith("#") or not line:  # Ignore comments and empty lines
            continue

        pixels = line.split(" ")
        for col, pixel in enumerate(pixels):
            if col < cols and row < rows:
                pixel_colors[row, col] = COLOR_MAP.get(pixel, (0.0, 0.0, 0.0))  # Default to black
        row += 1  # Increment row only for valid lines

    return pixel_colors
