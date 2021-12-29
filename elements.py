from pygame import draw, Rect
from static import *
from colours import *


class Button:
    buttons = []  # All the buttons created are stored here
    option = None

    def __init__(self, name, icon, x, y, length=STD_BUTTON_SIZE, width=STD_BUTTON_SIZE):
        self.name = name
        self.button = Rect(x, y, length, width)
        self.icon = icon
        Button.buttons.append(self)

    @classmethod
    def group_member(cls, button):
        name = getattr(button, 'name').split(":")
        if name[1] == cls.option or name[0] == cls.option:
            return True
        return False

    @classmethod
    def manager(cls, screen, option, mouse_x, mouse_y, mouse_b) -> str:
        cls.option = option
        group = list(filter(cls.group_member, cls.buttons))

        for button in group:
            cls.draw_icon(screen, button)
            cls.draw_border(screen, button, mouse_x, mouse_y, mouse_b)

        for button in group:
            name = getattr(button, 'name').split(":")
            output = cls.check_press(name[1], button, mouse_x, mouse_y, mouse_b)
            if output is not None:
                output = "option:" + output if name[0] == "option" else output
                return output

    @classmethod
    def draw_border(cls, screen, button, mouse_x, mouse_y, mouse_b, ):
        button = getattr(button, 'button')
        if button.collidepoint(mouse_x, mouse_y) and mouse_b[0] == 1:
            draw.rect(screen, BLACK, button, STD_WIDTH)
        elif button.collidepoint(mouse_x, mouse_y):
            draw.rect(screen, DULL_RED, button, STD_WIDTH)
        else:
            draw.rect(screen, DARK_GREY, button, STD_WIDTH)

    @classmethod
    def check_press(cls, name, button, mouse_x, mouse_y, mouse_b) -> str:
        button = getattr(button, 'button')
        if button.collidepoint(mouse_x, mouse_y) and mouse_b[0] == 1:
            return name

    @classmethod
    def draw_icon(cls, screen, button):
        icon = getattr(button, 'icon')
        button = getattr(button, 'button')
        x, y, l, w = button  # Decompose button and apply offset
        screen.blit(icon, (x + STD_WIDTH * 2, y + STD_WIDTH * 2, l, w))


class Bar:  # Can be used as a nav bar or a sidebar
    def __init__(self, length, width, x=0, y=0):
        self.bar = Rect(x, y, length, width)

    def draw_bar(self, screen):
        draw.rect(screen, LIGHT_GREY, self.bar)


class Canvas:  # For the paint program - the background canvas that will be updated
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


class DropMenu:
    menu = None

    def __init__(self, x, y, length, width):
        DropMenu.menu = Rect(x, y, length, width)

    @classmethod
    def draw_drop_menu(cls, screen):
        draw.rect(screen, GREY, cls.menu)

    @classmethod
    def draw_menu_collision(cls):
        pass


def decorator_function(input_function):
    for i in Button.buttons:
        menu_flag = False
        button = getattr(i, 'button')
        name = getattr(i, 'name').split(":")
        icon = getattr(i, 'icon')

        if name[1] == Button.option:
            menu_flag = True
            pass
        elif name[0] != Button.option:
            continue

        def wrapper_function(*args, **kwargs):
            input_function(*args, **kwargs)

        return wrapper_function
