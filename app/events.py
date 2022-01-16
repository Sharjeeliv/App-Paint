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

    def is_valid_option(self):
        return self.group != 'option' and self.option is not None

    def draw_on_canvas(self):
        # All tools will be based on coordinates, so we update it in the parent class resulting in fewer child params
        self.current_tool.update_internal_variables(self.mouse_cords, self.prev_mouse_cords,
                                                    self.canvas.get_parent_offset)
        # Validation is handled outside the particular tool function to reduce clutter
        if self.primary_mouse_click() and self.canvas.on_canvas(self.mouse_cords) and self.is_valid_option():
            self.current_tool.draw_to_screen(self.canvas, self.mouse_cords, self.prev_mouse_cords, 10, (0, 0, 0))

    def change_tool(self, option):
        if option is None or TOOLS.get(option) is None:
            return
        elif option is not None and "stamp" in option:
            self.current_tool = TOOLS.get('stamps')
        else:
            self.current_tool = TOOLS.get(option)
