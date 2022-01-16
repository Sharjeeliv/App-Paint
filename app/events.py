from pygame import mouse, event, QUIT
from .tools import *


class Events:
    """
    Events is a superclass to stage because the stage is set based on what events are happening
    """
    PRIMARY = 1

    def __init__(self):
        self.prev_mouse_cords = 0, 0
        self.mouse_cords = 0, 0
        self.mouse_button = None  # Button data is received as an array, so it is kept separate for simplicity

        # Program state variables
        self.group, self.option, self.canvas = "draw", None, None
        self.run_program = True
        self.current_tool = Pencil()

    def refresh_mouse(self):
        self.prev_mouse_cords = self.mouse_cords
        self.mouse_cords = mouse.get_pos()
        self.mouse_button = mouse.get_pressed()

    def primary_mouse_click(self):
        return self.mouse_button[self.PRIMARY] == 1

    def button_element_click(self):
        pass

    def draw_on_canvas(self):
        if self.primary_mouse_click() and self.canvas.on_canvas(self.mouse_cords) and self.group != 'option':
            self.current_tool.draw_to_screen(self.screen, self.mouse_cords, self.prev_mouse_cords)

    def event_manager(self):
        pass
