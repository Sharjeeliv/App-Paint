from pygame import Rect, draw

LIGHT_GREY = (220, 220, 220)


class Bar:  # Can be used as a nav bar or a sidebar

    def __init__(self, length, width, x=0, y=0):
        self.bar = Rect(x, y, length, width)

    def draw_bar(self, screen):
        draw.rect(screen, LIGHT_GREY, self.bar)
