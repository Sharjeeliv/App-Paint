import abc
from abc import ABC, abstractmethod


class Tool(ABC):
    """
    In a paint program there is only ever 1 tool, the form changes but there is only one tool.
    Due to which this class will consist of no instances since for example, a pen is not its own instance
    of a tool. Instead, it is a tool that has a different implementation
    """

    def __init__(self, mouse_x, mouse_y, prev_mouse_x, prev_mouse_y):
        pass

    @classmethod
    def calculate_distance(cls, mouse_x, mouse_y, prev_mouse_x, prev_mouse_y) -> (int, int):
        return prev_mouse_x - mouse_x, prev_mouse_y - mouse_y

    @abc.abstractmethod
    def draw_to_screen(self, canvas, mouse_x, mouse_y, prev_mouse_x, prev_mouse_y):

        """
        This method takes in the canvas and will draw the final 'object' to the screen.
        for example, for a brush tool it will draw the one specific stroke
        :return: void
        """
        print('active internal')

