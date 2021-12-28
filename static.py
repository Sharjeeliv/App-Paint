from pygame import image, transform

# General Constants
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
STD_WIDTH = 4



"""class Icons:
    TITLE = transform.rotate(transform.scale(image.load("Images/side_icons/Title.png"), (200, 50)), 270)

    # Side Menu Button Icons
    # ---------------------------------------------------------
    COLOUR = transform.scale(image.load("Images/side_icons/Colour.png"), (64, 64))
    OPACITY = transform.scale(image.load("Images/side_icons/Opacity.png"), (64, 64))
    WIDTH = transform.scale(image.load("Images/side_icons/Width.png"), (64, 64))
    SAVE = transform.scale(image.load("Images/side_icons/Save.png"), (32, 32))
    LOAD = transform.scale(image.load("Images/side_icons/Load.png"), (32, 32))

    RED_SLIDER = transform.scale(image.load("Images/side_icons/ColourSliders/RSlider.png"), (20, 255))
    GREEN_SLIDER = transform.scale(image.load("Images/side_icons/ColourSliders/GSlider.png"), (20, 255))
    BLUE_SLIDER = transform.scale(image.load("Images/side_icons/ColourSliders/BSlider.png"), (20, 255))
    CHECK_MARK = transform.scale(image.load("Images/Shapes/CheckMark.png"), (16, 16))

    # Draw Menu Button Icons
    # ---------------------------------------------------------
    DRAW = transform.scale(image.load("Images/Drawing/Drawing.png"), (64, 64))
    FOUNT_PEN = transform.scale(image.load("Images/Drawing/FountainPen.png"), (64, 64))
    MARKER = transform.scale(image.load("Images/Drawing/Marker.png"), (64, 64))
    PENCIL = transform.scale(image.load("Images/Drawing/Pencil.png"), (64, 64))

    # Paint Menu Button Icons
    # ---------------------------------------------------------
    PAINT = transform.scale(image.load("Images/Painting/Painting.png"), (64, 64))
    BRUSH = transform.scale(image.load("Images/Painting/PaintBrush.png"), (64, 64))
    SPRAY = transform.scale(image.load("Images/Painting/SprayPaint.png"), (64, 64))

    # Erase Menu Button Icons
    # ---------------------------------------------------------
    ERASE = transform.scale(image.load("Images/Erasing/EraserFamily.png"), (64, 64))
    ERASER = transform.scale(image.load("Images/Erasing/Eraser.png"), (64, 64))
    CLEAR = transform.scale(image.load("Images/Erasing/Clear.png"), (64, 64))

    # Shapes Menu Button Icons
    # ---------------------------------------------------------
    SHAPES = transform.scale(image.load("Images/Shapes/Shapes.png"), (64, 64))
    CIRCLE = transform.scale(image.load("Images/Shapes/Circle.png"), (64, 64))
    SQUARE = transform.scale(image.load("Images/Shapes/Square.png"), (64, 64))
    LINE = transform.scale(image.load("Images/Shapes/Line.png"), (64, 64))
    ELLIPSE = transform.scale(image.load("Images/Shapes/Ellipse.png"), (64, 64))

    # Stamp Menu Button Icons
    # ---------------------------------------------------------
    STAMP = transform.scale(image.load("Images/Stamps/Stamps.png"), (64, 64))
    STAMP_1 = transform.scale(image.load("Images/Stamps/Sun.png"), (64, 64))
    STAMP_2 = transform.scale(image.load("Images/Stamps/Cloud.png"), (64, 64))
    STAMP_3 = transform.scale(image.load("Images/Stamps/Rain.png"), (64, 64))
    STAMP_4 = transform.scale(image.load("Images/Stamps/Mountain.png"), (64, 64))
    STAMP_5 = transform.scale(image.load("Images/Stamps/Grass.png"), (64, 64))
    STAMP_6 = transform.scale(image.load("Images/Stamps/Trees.png"), (64, 64))

    # Settings Menu Button Icons
    # ---------------------------------------------------------
    SETTINGS = transform.scale(image.load("Images/Settings/Settings.png"), (64, 64))
    EXIT = transform.scale(image.load("Images/Settings/ForceExit.png"), (64, 64))"""


class Colours:
    LIGHT_GRAY = (220, 220, 220)
    BORDER = (100, 100, 100)
    HIGHLIGHT = (200, 70, 70)
    PRESS = (0, 0, 0)
