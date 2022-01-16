from pygame import draw, Surface, SRCALPHA

from .tools import Tool


class Pencil(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=255, variant=0):
        path = self.calculate_path(size)
        for position in path:
            draw.circle(canvas.get_surface, colour, position, 10)


class Marker(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=255, variant=0):
        path = self.calculate_path(size)
        for position in path:
            marker_head = Surface((size, size), SRCALPHA)
            marker_head.set_alpha(10)
            marker_head.fill(colour)
            if not self.same_position():
                canvas.get_surface.blit(marker_head, position)


class FountainPen(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=255, variant=0):
        pen_size, pen_stroke = size, 0
        while pen_size != 0:
            pen_size -= 1
            pen_stroke += 1
            draw.line(canvas.get_surface, colour, (self.prev_mouse_x + pen_stroke, self.prev_mouse_y + pen_stroke),
                      (self.mouse_x + pen_stroke, self.mouse_y + pen_stroke))
