from random import randint

from pygame import draw

from .tools import Tool


class Brush(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=0):
        pass


class Spray(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=0):

        random_position_x, random_position_y = randint(-size, size), randint(-size, size)
        if (random_position_x ** 2) + (random_position_y ** 2) <= size ** 2:
            draw.circle(canvas, colour, (self.mouse_x + random_position_x, self.mouse_y + random_position_y), 2)
