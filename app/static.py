from pygame import image, transform

# General Constants
STD_WIDTH = 4
STD_BORDER = 10
STD_BUTTON_SIZE = 80
TIPS = [
    "Left click to draw.",
    "Left click to erase.",
    "Left click to set marker.",
    "Shift/Left click to draw shape.",
    "Keep holding Left click and move to drag.",
    "Left click to place stamp.",

    "The size and color are adjustable.",
    "The size and opacity are adjustable.",
    "The size, colour and opacity are adjustable.",
    "The size is adjustable.",

    "The canvas will be cleared (filled white).",
    "Left click to exit program.",
    "Left click to set current color as point 1 color.",
    "Left click to set current color as point 2 color.",
    "Click the checkbox on the right to toggle fill.",
]

# Side Menu Button Icons
# ---------------------------------------------------------
COLOUR = transform.scale(image.load("app/static/side_icons/colour.png"), (32, 32))
OPACITY = transform.scale(image.load("app/static/side_icons/opacity.png"), (32, 32))
WIDTH = transform.scale(image.load("app/static/side_icons/width.png"), (32, 32))
SAVE = transform.scale(image.load("app/static/side_icons/save.png"), (32, 32))
LOAD = transform.scale(image.load("app/static/side_icons/load.png"), (32, 32))
UNDO = transform.scale(image.load("app/static/side_icons/undo.png"), (32, 32))
REDO = transform.flip(UNDO, True, False)

RED_SLIDER = transform.scale(image.load("app/static/side_icons/slider_red.png"), (20, 255))
GREEN_SLIDER = transform.scale(image.load("app/static/side_icons/slider_green.png"), (20, 255))
BLUE_SLIDER = transform.scale(image.load("app/static/side_icons/slider_blue.png"), (20, 255))
CHECK_MARK = transform.scale(image.load("app/static/icons/check_mark.png"), (16, 16))

# Navigation Bar Button Icons
# ---------------------------------------------------------
DRAW = transform.scale(image.load("app/static/nav_bar_icons/drawing.png"), (64, 64))
PAINT = transform.scale(image.load("app/static/nav_bar_icons/painting.png"), (64, 64))
ERASE = transform.scale(image.load("app/static/nav_bar_icons/erasing.png"), (64, 64))
SHAPES = transform.scale(image.load("app/static/nav_bar_icons/shapes.png"), (64, 64))
STAMPS = transform.scale(image.load("app/static/nav_bar_icons/stamps.png"), (64, 64))
SETTINGS = transform.scale(image.load("app/static/nav_bar_icons/settings.png"), (64, 64))

# Tool Button Icons
# ---------------------------------------------------------
FOUNT_PEN = transform.scale(image.load("app/static/icons/fountain_pen.png"), (64, 64))
MARKER = transform.scale(image.load("app/static/icons/marker.png"), (64, 64))
PENCIL = transform.scale(image.load("app/static/icons/pencil.png"), (64, 64))

BRUSH = transform.scale(image.load("app/static/icons/paint_brush.png"), (64, 64))
SPRAY = transform.scale(image.load("app/static/icons/spray_paint.png"), (64, 64))

ERASER = transform.scale(image.load("app/static/icons/eraser.png"), (64, 64))
CLEAR = transform.scale(image.load("app/static/icons/clear.png"), (64, 64))

CIRCLE = transform.scale(image.load("app/static/icons/circle.png"), (64, 64))
SQUARE = transform.scale(image.load("app/static/icons/square.png"), (64, 64))
LINE = transform.scale(image.load("app/static/icons/line.png"), (64, 64))
ELLIPSE = transform.scale(image.load("app/static/icons/ellipse.png"), (64, 64))

STAMP_1 = transform.scale(image.load("app/static/icons/stamp_sun.png"), (64, 64))
STAMP_2 = transform.scale(image.load("app/static/icons/stamp_cloud.png"), (64, 64))
STAMP_3 = transform.scale(image.load("app/static/icons/stamp_rain.png"), (64, 64))
STAMP_4 = transform.scale(image.load("app/static/icons/stamp_mountain.png"), (64, 64))
STAMP_5 = transform.scale(image.load("app/static/icons/stamp_grass.png"), (64, 64))
STAMP_6 = transform.scale(image.load("app/static/icons/stamp_trees.png"), (64, 64))

EXIT = transform.scale(image.load("app/static/icons/force_exit.png"), (64, 64))
