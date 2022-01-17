from pygame import font, display, event, QUIT

from app.static.colours import *
from .app_elements import Button, DropMenu
from .events import Events
from .gui_elements.bars import Bar
from .gui_elements.canvas import Canvas

'''
The stage module is responsible for "staging" the app/game and hence is usually
present in all programs. It's primary responsibilities are to control the flow (direct the play),
and layout the gui (set the stage).
'''

"""
It inherits from the events class as the stage of the game depends on the events.
"""


class Stage:
    PRIMARY = 0

    def __init__(self):
        super().__init__()

        # Initialize display and screen variables
        self.WINDOW_LENGTH, self.WINDOW_WIDTH = 1280, 720
        display.set_caption("Simply Paint")
        self.screen = display.set_mode((self.WINDOW_LENGTH, self.WINDOW_WIDTH))
        Events.screen = self.screen  # Update screen stored in that class

        # Program gui element setup
        self.drop_menu = DropMenu(5, 5, 90, 630)
        self.top_bar = Bar(self.WINDOW_LENGTH, 100)
        self.side_bar = Bar(100, self.WINDOW_WIDTH, self.WINDOW_LENGTH - 60)
        Events.canvas = Canvas(self.screen, 10, 110, self.WINDOW_LENGTH - 80, self.WINDOW_WIDTH - 110)
        Events.canvas.store_canvas()

    @property
    def get_screen(self):
        return self.screen

    def static_layout(self):
        self.screen.fill(DARK_GREY)  # Program background
        self.top_bar.draw_bar(self.screen)
        self.side_bar.draw_bar(self.screen)

    def dynamic_layout(self):  # This manages the option dropdown refresh
        if Events.option is not None:
            if Events.option == "option" and self.drop_menu.draw_menu_collision(Events.mouse_cords):
                temp = self.drop_menu.draw_drop_menu(self.screen, Events.mouse_cords, Events.mouse_button)
                self.update_group_and_option(temp)
            elif not self.drop_menu.draw_menu_collision(Events.mouse_cords):
                if Events.option == "option":
                    Events.option = None

    @staticmethod
    def update_group_and_option(input_package):
        if input_package is not None:
            input_option = input_package.split(":")
            group = input_option[0]
            option = input_option[1]

            if group == "option":
                Events.group = option
                Events.option = group  # The tool we use is the option
                if option != "option":
                    Button.update_icon(Events.group)
            else:
                Events.option = option
        Events.change_tool()

    def event_manager(self):
        # Refresh mouse information
        Events.refresh_mouse()
        Events.canvas.update_canvas(self.screen)
        Events.draw_on_canvas()

        # Refresh canvas information
        Events.canvas.store_canvas()

        # Button event
        received_package = Button.manager(self.screen, Events.group, Events.mouse_cords, Events.mouse_button)
        self.update_group_and_option(received_package)

        self.dynamic_layout()

        for evt in event.get():
            if evt.type == QUIT:
                Events.run_program = False

        # Event interruptions

    def run(self):
        while Events.run_program:
            # --------------------------
            self.static_layout()
            self.event_manager()

            # --------------------------
            # time.delay(16)
            display.flip()
        font.quit()
        quit()
