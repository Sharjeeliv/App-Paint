# Memento Patter: Originator

from pygame import Rect
from . import WHITE


class Canvas:  # For the app program - the background canvas that will be updated
    def __init__(self, screen, x, y, length, width):
        self._initial_frame, self.current_frame = True, None  # Canvas states
        self._object = Rect(x, y, length, width)
        self._canvas = screen.subsurface(self._object)
        self._canvas.fill(WHITE)

    def store_canvas(self):
        self.current_frame = self._canvas.copy()
        self.initial_frame = False

    def update_canvas(self, screen):
        if not self.initial_frame:
            screen.blit(self.current_frame, self._object)

    def on_canvas(self, mouse) -> bool:
        return self._object.collidepoint(mouse)
