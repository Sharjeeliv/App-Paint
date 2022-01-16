from .draw import *
from .erase import *
from .paint import *
from .shapes import *
from .stamps import *
from .tools import Tool

# We import the classes as to reduce clutter and improve readability
# A benefit of this approach is that if we decide to add more tools we only
# need to add the import and class in this file to add its functionality.
# However, the user will still need to add the icon (for the button)
# in the static file and create a button object in the app __init__ file

__all__ = ['Pencil', 'Marker', 'FountainPen', 'Brush', 'Spray', 'Eraser', 'Clear',
           'Circle', 'Square', 'Line', 'Ellipse', 'Stamps']
