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
    prev_mouse_cords = 0, 0
    mouse_cords = 0, 0
    mouse_button = None  # Button data is received as an array, so it is kept separate for simplicity

    # Program state variables
    group, option, canvas = "draw", None, None
    run_program = True
    current_tool = TOOLS.get('pencil')

    @classmethod
    def refresh_mouse(cls):
        cls.prev_mouse_cords = cls.mouse_cords
        cls.mouse_cords = mouse.get_pos()
        cls.mouse_button = mouse.get_pressed()

    @classmethod
    def primary_mouse_click(cls):
        return cls.mouse_button[PRIMARY] == 1

    @classmethod
    def button_element_click(cls):
        pass

    @classmethod
    def is_valid_option(cls):
        return cls.group != 'option' and cls.option is not None

    @classmethod
    def draw_on_canvas(cls):
        if cls.canvas is None:
            return
        # All tools will be based on coordinates, so we update it in the parent class resulting in fewer child params
        cls.current_tool.update_internal_variables(cls.mouse_cords, cls.prev_mouse_cords,
                                                   cls.canvas.get_parent_offset)
        # Validation is handled outside the particular tool function to reduce clutter
        if cls.primary_mouse_click() and cls.canvas.on_canvas(cls.mouse_cords) and cls.is_valid_option():
            print(type(cls.current_tool) is Stamps)
            cls.current_tool.draw_to_screen(cls.canvas, 50, (0, 0, 0))

    @classmethod
    def change_tool(cls, option):
        if option is None or TOOLS.get(option) is None:
            return
        elif option is not None and "stamp" in option:
            cls.current_tool = TOOLS.get('stamps')
        else:
            cls.current_tool = TOOLS.get(option)
