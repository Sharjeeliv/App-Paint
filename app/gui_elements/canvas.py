# Memento Patter: Originator

from pygame import Rect

WHITE = (255, 255, 255)


class Canvas:  # For the app program - the background canvas that will be updated
    def __init__(self, screen, x, y, length, width):
        self._offset_x, self._offset_y = x, y
        self._initial_frame, self._current_frame = True, None  # Canvas states
        self._object = Rect(x, y, length, width)
        self._canvas = screen.subsurface(self._object)
        self._canvas.fill(WHITE)

    @property
    def get_surface(self):
        return self._canvas

    @property
    def get_parent_offset(self):
        return self._offset_x, self._offset_y

    def store_canvas(self):
        self._current_frame = self._canvas.copy()
        self._initial_frame = False

    def update_canvas(self, screen):
        if not self._initial_frame:
            screen.blit(self._current_frame, self._object)

    def on_canvas(self, mouse) -> bool:
        return self._object.collidepoint(mouse)
