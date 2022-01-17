import pygame.transform

import app.static as static
from .tools import Tool


class Stamps(Tool):
    def draw_to_screen(self, canvas, size, colour, opacity=0, variant=""):
        # Get particular stamp
        stamp = str(variant).upper()
        stamp = getattr(static, stamp)
        stamp = pygame.transform.scale(stamp, (size, size))

        # display it at current mouse position
        canvas.get_surface.blit(stamp, (self.mouse_x, self.mouse_y))
