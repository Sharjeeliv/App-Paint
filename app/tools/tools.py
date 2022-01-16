import abc
from abc import ABC
from math import sqrt


class Tool(ABC):
    """
    In a paint program there is only ever 1 tool, the form changes but there is only one tool.
    Due to which this class will consist of no instances since for example, a pen is not its own instance
    of a tool. Instead, it is a tool that has a different implementation
    """

    def __init__(self):
        pass

    @classmethod
    def calculate_distance(cls, mouse_cords, prev_mouse_cords) -> (int, int):
        prev_mouse_x, prev_mouse_y = prev_mouse_cords
        mouse_x, mouse_y = mouse_cords
        return mouse_x - prev_mouse_x, mouse_y - prev_mouse_y

    @classmethod
    def calculate_path(cls, mouse_cords, prev_mouse_cords, size) -> (int, int):
        distance_x, distance_y = cls.calculate_distance(mouse_cords, prev_mouse_cords)
        distance = sqrt((distance_x ** 2) + (distance_y ** 2))
        distance = int(distance)
        generated_path = cls.generate_path_cords(distance, prev_mouse_cords, distance_x, distance_y, size)
        return generated_path

    @classmethod  # Generator
    def generate_path_cords(cls, distance, prev_mouse_cords, distance_x, distance_y, size):
        prev_mouse_x, prev_mouse_y = prev_mouse_cords
        for i in range(distance):
            position_x = (prev_mouse_x + round(((i / distance) * distance_x))) - round(size / 2)
            position_y = (prev_mouse_y + round(((i / distance) * distance_y))) - round(size / 2)
            yield position_x, position_y

    @abc.abstractmethod
    def draw_to_screen(self, canvas, mouse_cords, prev_mouse_cords):
        """
        This method takes in the canvas and will draw the final 'object' to the screen.
        for example, for a brush tool it will draw the one specific stroke
        :return: void
        """
        print('active internal')



