from pygame import mouse

from .tools import *

PRIMARY = 0
TOOLS = {
    'pencil': Pencil(),
    'marker': Marker(),
    'fount_pen': FountainPen(),
    'brush': Brush(),
    'spray': Spray(),
    'eraser': Eraser(),
    'clear': Clear(),
    'circle': Circle(),
    'square': Square(),
    'line': Line(),
    'ellipse': Ellipse(),
    'stamps': Stamps()  # The numbers will be parsed and sent as input data
}


class Events:
    """
    Events is a superclass to stage because the stage is set based on what events are happening
    """

    def __init__(self):
        self.prev_mouse_cords = 0, 0
        self.mouse_cords = 0, 0
        self.mouse_button = None  # Button data is received as an array, so it is kept separate for simplicity

        # Program state variables
        self.group, self.option, self.canvas = "draw", None, None
        self.run_program = True
        self.current_tool = TOOLS.get('pencil')

    def refresh_mouse(self):
        self.prev_mouse_cords = self.mouse_cords
        self.mouse_cords = mouse.get_pos()
        self.mouse_button = mouse.get_pressed()

    def primary_mouse_click(self):
        return self.mouse_button[PRIMARY] == 1

    def button_element_click(self):
        pass

    def draw_on_canvas(self, screen):
        if self.primary_mouse_click() and self.canvas.on_canvas(self.mouse_cords) and self.group != 'option':
            self.current_tool.draw_to_screen(screen, self.mouse_cords, self.prev_mouse_cords)

    def change_tool(self, option):
        if option is None:
            return
        elif option is not None and "stamp" in option:
            self.current_tool = TOOLS.get('stamps')
        else:
            self.current_tool = TOOLS.get(option)


