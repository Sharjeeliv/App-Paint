from pygame import draw, Rect
import app.static as static
from app.graphic_elements import button as btn
from app.colours import *


class Button(btn.Button):

    @classmethod
    def _group_member(cls, button):
        name = getattr(button, 'name').split(":")
        if name[0] == cls._option or name[1] == "general" or name[0] == "static":
            return True
        return False

    @classmethod
    def update_icon(cls, icon):
        for button in cls._buttons:
            name = getattr(button, 'name')
            print(f"temp is {name}")
            if name == "option:general" and icon != "general":
                temp = str(icon).upper()
                print(f"temp is {temp}")
                temp = getattr(static, temp)
                setattr(button, "icon", temp)

    @classmethod
    def manager(cls, screen, option, mouse_x, mouse_y, mouse_b) -> str:
        cls._option = option
        group = list(filter(cls._group_member, cls._buttons))

        # Refresh buttons
        for button in group:
            cls._draw_icon(screen, button)
            cls._draw_border(screen, button, mouse_x, mouse_y, mouse_b)

        # Detect a button press
        for button in group:
            name = getattr(button, 'name')
            output = cls._check_press(name, button, mouse_x, mouse_y, mouse_b)
            if output is not None:
                return output


class DropMenu:
    menu = None

    def __init__(self, x, y, length, width):
        DropMenu.menu = Rect(x, y, length, width)

    @classmethod
    def draw_drop_menu(cls, screen, mouse_x, mouse_y, mouse_b):
        draw.rect(screen, GREY, cls.menu)
        temp = Button.manager(screen, "option", mouse_x, mouse_y, mouse_b)
        if temp is not None:
            return temp

    @classmethod
    def draw_menu_collision(cls, mouse_x, mouse_y):
        if cls.menu.collidepoint(mouse_x, mouse_y):
            return True
