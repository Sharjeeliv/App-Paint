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

            # Special handling for an option button that bypassing normal button handling

            cls.draw_icon(screen, button, icon)
            output = cls.check_collision_and_draw_border(screen, name, button, mouse_x, mouse_y, mouse_b)
            if output is not None: return output

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


class Bar:  # Can be used as a nav bar or a sidebar
    def __init__(self, length, width, x=0, y=0):
        self.bar = Rect(x, y, length, width)

    def draw_bar(self, screen):
        draw.rect(screen, Colours.GREY, self.bar)


class Canvas:  # For the paint program - the background canvas that will be updated
    def __init__(self, screen, x, y, length, width):
        self.initial_frame, self.current_frame = True, None  # Canvas states
        self.position = Rect(x, y, length, width)
        self.canvas = screen.subsurface(self.position)
        self.canvas.fill(Colours.WHITE)

    def store_canvas(self):
        self.current_frame = self.canvas.copy()
        self.initial_frame = False

    def update_canvas(self, screen):
        if not self.initial_frame:
            screen.blit(self.current_frame, self.position)


class DropMenu:
    menu = None

    def __init__(self, x, y, length, width):
        DropMenu.menu = Rect(x, y, length, width)

    @classmethod
    def draw_drop_menu(cls, screen):
        draw.rect(screen, Colours.GREY, cls.menu)

    @classmethod
    def draw_menu_collision(cls):
        pass
