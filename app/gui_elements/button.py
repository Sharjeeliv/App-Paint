from pygame import Rect, draw


class Button:
    button_size = 80
    press_colour = (0, 0, 0)
    hover_colour = (200, 70, 70)
    rest_colour = (100, 100, 100)
    width = 4

    _buttons = []  # All the buttons created are stored here
    _option = None

    def __init__(self, name, icon, x, y, length=button_size, width=button_size):
        self.name = name
        self.button = Rect(x, y, length, width)
        self.icon = icon
        Button._buttons.append(self)

    @classmethod
    def manager(cls, screen, mouse_cords, mouse_button) -> str:

        # Refresh buttons
        for button in cls._buttons:
            cls._draw_border(screen, button, mouse_cords, mouse_button)

        # Detect a button press
        for button in cls._buttons:
            name = getattr(button, 'name')
            output = cls._check_press(name, button, mouse_cords, mouse_button)
            if output is not None:
                return output

    @classmethod
    def _draw_border(cls, screen, button, mouse_cords, mouse_button, ):
        button = getattr(button, 'button')
        if button.collidepoint(mouse_cords) and mouse_button[0] == 1:
            draw.rect(screen, cls.press_colour, button, cls.width)
        elif button.collidepoint(mouse_cords):
            draw.rect(screen, cls.hover_colour, button, cls.width)
        else:
            draw.rect(screen, cls.rest_colour, button, cls.width)

    @classmethod
    def _check_press(cls, name, button, mouse_cords, mouse_button) -> str:
        button = getattr(button, 'button')
        if button.collidepoint(mouse_cords) and mouse_button[0] == 1:
            return name

    @classmethod
    def _draw_icon(cls, screen, button):
        icon = getattr(button, 'icon')
        button = getattr(button, 'button')
        x, y, l, w = button  # Decompose button and apply offset
        screen.blit(icon, (x + cls.width * 2, y + cls.width * 2, l, w))
