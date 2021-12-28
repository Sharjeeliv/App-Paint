from pygame import draw, Rect
from static import *


class Button:
    buttons = []  # All the buttons created are stored here

    def __init__(self, name, icon, x, y, length=STD_BUTTON_SIZE, width=STD_BUTTON_SIZE, ):
        self.name = name
        self.button = Rect(x, y, length, width)
        self.icon = icon
        Button.buttons.append(self)

    @classmethod
    def manager(cls, screen, mouse_x, mouse_y, mouse_b) -> str:
        for i in cls.buttons:  # Iterate through all buttons once
            button = getattr(i, 'button')
            name = getattr(i, 'name')
            icon = getattr(i, 'icon')

            cls.draw_icon(screen, button, icon)
            output = cls.check_collision_and_draw_border(screen, name, button, mouse_x, mouse_y, mouse_b)
            if output is not None:return output

    @classmethod
    def check_collision_and_draw_border(cls, screen, name, button, mouse_x, mouse_y, mouse_b) -> str:
        if button.collidepoint(mouse_x, mouse_y) and mouse_b[0] == 1:
            draw.rect(screen, Colours.BLACK, button, STD_WIDTH)
            return name
        elif button.collidepoint(mouse_x, mouse_y):
            draw.rect(screen, Colours.RED, button, STD_WIDTH)
        else:
            draw.rect(screen, Colours.GREY, button, STD_WIDTH)

    @classmethod
    def draw_icon(cls, screen, button, icon):
        x, y, l, w = button  # Decompose button and apply offset
        screen.blit(icon, (x + STD_WIDTH * 2, y + STD_WIDTH * 2, l, w))


class Bar:  # Can be used as a nav bar or a side bar
    def __init__(self, length, width, x=0, y=0):
        self.bar = Rect(x, y, length, width)

    def draw_bar(self, screen):
        draw.rect(screen, Colours.GREY, self.bar)
