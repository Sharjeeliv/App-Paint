from pygame import draw

from .tools import Tool


class Pencil(Tool):
    TEMP_SIZE = 10
    BLACK = 0, 0, 0

    def __init__(self):
        super().__init__()

    def draw_to_screen(self, canvas, mouse_cords, prev_mouse_cords):
        path = self.calculate_path(mouse_cords, prev_mouse_cords, self.TEMP_SIZE)
        for position in path:
            draw.circle(canvas, self.BLACK, position, 10)


class Marker(Tool):
    def draw_to_screen(self, canvas, mouse_cords, prev_mouse_cords):
        pass


class FountainPen(Tool):
    def draw_to_screen(self, canvas, mouse_cords, prev_mouse_cords):
        pass
