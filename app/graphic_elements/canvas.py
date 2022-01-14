from pygame import Rect
from . import WHITE


class Canvas:  # For the app program - the background canvas that will be updated
    def __init__(self, screen, x, y, length, width):
        self.initial_frame, self.current_frame = True, None  # Canvas states
        self.position = Rect(x, y, length, width)
        self.canvas = screen.subsurface(self.position)
        self.canvas.fill(WHITE)

    def store_canvas(self):
        self.current_frame = self.canvas.copy()
        self.initial_frame = False

    def update_canvas(self, screen):
        if not self.initial_frame:
            screen.blit(self.current_frame, self.position)
