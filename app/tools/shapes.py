from pygame import draw

from .tools import Tool


class Square(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=0):
        if self.same_position():
            draw.rect(canvas.get_surface, colour, (self.mouse_x, self.mouse_y, size, size))


class Circle(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=0):
        if self.same_position():
            draw.circle(canvas.get_surface, colour, (self.mouse_x, self.mouse_y), size / 2)
        # We divide size by 2 so that the diameter is equal to the size


class Line(Tool):  # Temporary
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=0):
        draw.line(canvas.get_surface, colour, (self.prev_mouse_x, self.prev_mouse_y), (self.mouse_x, self.mouse_y),
                  size)


class Ellipse(Tool):  # Temporary
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=0):
        draw.ellipse(canvas.get_surface, colour, (self.prev_mouse_x, self.prev_mouse_y, self.mouse_x, self.mouse_y),
                     size)
