from math import ceil
from random import randint

from pygame import draw, SRCALPHA, Surface

from .tools import Tool


class Brush(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=0):
        red, green, blue = colour

        path = self.calculate_path(size)
        for position in path:
            brush_radius = ceil(size / 10) * 10  # Gives us nearest to 10
            # The loop provides a taper effect leading to lighter edges giving the impression of water paint
            while brush_radius != 0:
                brush_radius -= 10
                # Since the draw method does not display alpha, we implement the alpha by changing its value
                # on the surface on which the 'paint' is. Then by bliting it, we work around the draw limitation
                brush_head = Surface((brush_radius * 2, brush_radius * 2), SRCALPHA)
                draw.circle(brush_head, (red, green, blue, 10), (brush_radius, brush_radius), brush_radius)
                if not self.same_position():
                    position_x, position_y = position
                    canvas.get_surface.blit(brush_head, (position_x - brush_radius, position_y - brush_radius))


class Spray(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=0):
        for i in range(size):  # The amount of 'spray' is proportional to it's size
            random_position_x, random_position_y = randint(-size, size), randint(-size, size)
            if (random_position_x ** 2) + (random_position_y ** 2) <= size ** 2:
                draw.circle(canvas.get_surface, colour,
                            (self.mouse_x + random_position_x, self.mouse_y + random_position_y), 1)
