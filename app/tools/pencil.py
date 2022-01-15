from .tools import Tool
from math import sqrt
from pygame import draw


class Pencil(Tool):

    def __init__(self):
        pass

    def draw_to_screen(self, canvas, mouse_x, mouse_y, prev_mouse_x, prev_mouse_y):
        print('active internal --- 2')
        TEMP_SIZE = 10
        distance_x, distance_y = self.calculate_distance(mouse_x, mouse_y, prev_mouse_x, prev_mouse_y)

        distance = sqrt(distance_x ** 2 + distance_y ** 2)

        for i in range(round(distance)):
            position_x = (prev_mouse_x + round(((i / distance) * distance_x))) - round(TEMP_SIZE / 2)
            position_y = (prev_mouse_y + round(((i / distance) * distance_y))) - round(TEMP_SIZE / 2)

            draw.rect(canvas, (0, 0, 0), (position_x, position_y, TEMP_SIZE, TEMP_SIZE))
