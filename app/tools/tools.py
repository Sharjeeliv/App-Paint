import abc
from abc import ABC
from math import sqrt


class Tool(ABC):
    mouse_x, mouse_y = 0, 0
    prev_mouse_x, prev_mouse_y = 0, 0
    offset_x, offset_y = 0, 0

    """
    In a paint program there is only ever 1 tool, the form changes but there is only one tool.
    Due to which this class will consist of no instances since for example, a pen is not its own instance
    of a tool. Instead, it is a tool that has a different implementation
    """

    @classmethod
    def update_internal_variables(cls, mouse_cords, prev_mouse_cords, offset=(0, 0)):
        # Unpack variables
        cls.offset_x, cls.offset_y = offset
        cls.prev_mouse_x, cls.prev_mouse_y = prev_mouse_cords
        cls.mouse_x, cls.mouse_y = mouse_cords

        #  Apply offset
        cls.prev_mouse_x, cls.prev_mouse_y = cls.prev_mouse_x - cls.offset_x, cls.prev_mouse_y - cls.offset_y
        cls.mouse_x, cls.mouse_y = cls.mouse_x - cls.offset_x, cls.mouse_y - cls.offset_y

    @classmethod
    def calculate_distance(cls) -> (int, int):
        return cls.mouse_x - cls.prev_mouse_x, cls.mouse_y - cls.prev_mouse_y

    @classmethod
    def calculate_path(cls, size) -> (int, int):
        distance_x, distance_y = cls.calculate_distance()
        distance = int(sqrt((distance_x ** 2) + (distance_y ** 2)))
        generated_path = cls.generate_path_cords(distance, distance_x, distance_y, size)
        return generated_path

    @classmethod  # Generator
    def generate_path_cords(cls, distance, distance_x, distance_y, size):
        for i in range(distance):
            print(size, " is size")
            position_x = (cls.prev_mouse_x + round(((i / distance) * distance_x))) - round(size / 2)
            position_y = (cls.prev_mouse_y + round(((i / distance) * distance_y))) - round(size / 2)
            yield position_x, position_y

    @abc.abstractmethod
    def draw_to_screen(self, canvas, size, colour, opacity, variant=0):
        """
        This method takes in the canvas and will draw the final 'object' to the screen.
        for example, for a brush tool it will draw the one specific stroke
        :return: void
        """
