from pygame import draw

from .tools import Tool

WHITE = (255, 255, 255)


class Eraser(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=0):
        path = self.calculate_path(size)
        for position in path:
            draw.circle(canvas.get_surface, WHITE, position, 10)


class Clear(Tool):
    def draw_to_screen(self, canvas, mouse_cords, prev_mouse_cords, size, colour, opacity=0, variant=0):
        canvas.get_surface.fill(WHITE)  # We fill the area (10, 110, 1200, 610)
