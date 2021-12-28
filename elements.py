from pygame import draw, Rect
from static import *


class Button:
    buttons = []  # All the buttons created are stored here

    def __init__(self, name, x, y, length=80, width=80):
        self.name = name
        self.button = Rect(x, y, length, width)
        Button.buttons.append(self)

    @classmethod
    def manager(cls, screen, mouse_x, mouse_y, mouse_b) -> str:
        for i in cls.buttons:  # Iterate through all buttons once
            button = getattr(i, 'button')
            name = getattr(i, 'name')
            cls.insert_icon(screen, button)
            output = cls.check_collision(screen, name, button, mouse_x, mouse_y, mouse_b)
            if output is not None:
                return output

    @classmethod
    def check_collision(cls, screen, name, button, mouse_x, mouse_y, mouse_b) -> str:
        if button.collidepoint(mouse_x, mouse_y) and mouse_b[0] == 1:
            draw.rect(screen, Colours.PRESS, button, STD_WIDTH)
            return name
        elif button.collidepoint(mouse_x, mouse_y):
            draw.rect(screen, Colours.HIGHLIGHT, button, STD_WIDTH)
        else:
            draw.rect(screen, Colours.BORDER, button, STD_WIDTH)

    @classmethod
    def insert_icon(cls, screen, button):
        pass
