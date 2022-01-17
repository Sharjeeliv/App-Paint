from app.gui_elements.slider import Slider
from app.static import RED_SLIDER, BLUE_SLIDER, GREEN_SLIDER


class Colour:
    red_slider = Slider(RED_SLIDER, (1380, 580))
    green_slider = Slider(GREEN_SLIDER, (1400, 580))
    blue_slider = Slider(BLUE_SLIDER, (1420, 580))

    @classmethod
    def draw_interface(cls, screen):
        cls.red_slider.draw_slider(screen)

    @classmethod
    def colour_option_interface(cls):
        pass

