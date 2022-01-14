from app.graphic_elements import STD_BUTTON_SIZE, STD_WIDTH, STD_REST_COLOUR, STD_HOVER_COLOUR, STD_PRESS_COLOUR
from pygame import Rect, draw


class Button:
    _buttons = []  # All the buttons created are stored here
    _option = None

    def __init__(self, name, icon, x, y, length=STD_BUTTON_SIZE, width=STD_BUTTON_SIZE):
        self.name = name
        self.button = Rect(x, y, length, width)
        self.icon = icon
        Button._buttons.append(self)

    @classmethod
    def manager(cls, screen, mouse_x, mouse_y, mouse_b) -> str:

        # Refresh buttons
        for button in cls._buttons:
            cls._draw_border(screen, button, mouse_x, mouse_y, mouse_b)

        # Detect a button press
        for button in cls._buttons:
            name = getattr(button, 'name')
            output = cls._check_press(name, button, mouse_x, mouse_y, mouse_b)
            if output is not None:
                return output

    @classmethod
    def _draw_border(cls, screen, button, mouse_x, mouse_y, mouse_b, ):
        button = getattr(button, 'button')
        if button.collidepoint(mouse_x, mouse_y) and mouse_b[0] == 1:
            draw.rect(screen, STD_PRESS_COLOUR, button, STD_WIDTH)
        elif button.collidepoint(mouse_x, mouse_y):
            draw.rect(screen, STD_HOVER_COLOUR, button, STD_WIDTH)
        else:
            draw.rect(screen, STD_REST_COLOUR, button, STD_WIDTH)

    @classmethod
    def _check_press(cls, name, button, mouse_x, mouse_y, mouse_b) -> str:
        button = getattr(button, 'button')
        if button.collidepoint(mouse_x, mouse_y) and mouse_b[0] == 1:
            return name

    @classmethod
    def _draw_icon(cls, screen, button):
        icon = getattr(button, 'icon')
        button = getattr(button, 'button')
        x, y, l, w = button  # Decompose button and apply offset
        screen.blit(icon, (x + STD_WIDTH * 2, y + STD_WIDTH * 2, l, w))
