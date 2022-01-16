from pygame import font, display, event, QUIT

from app.static.colours import *
from .elements import Button, DropMenu
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


class Stage(Events):
    PRIMARY = 0

    def __init__(self):
        super().__init__()

        # Initialize display and screen variables
        self.WINDOW_LENGTH, self.WINDOW_WIDTH = 1280, 720
        display.set_caption("Simply Paint")
        self.screen = display.set_mode((self.WINDOW_LENGTH, self.WINDOW_WIDTH))

        # Program gui element setup
        self.drop_menu = DropMenu(5, 5, 90, 630)
        self.top_bar = Bar(self.WINDOW_LENGTH, 100)
        self.side_bar = Bar(100, self.WINDOW_WIDTH, self.WINDOW_LENGTH - 60)
        self.canvas = Canvas(self.screen, 10, 110, self.WINDOW_LENGTH - 80, self.WINDOW_WIDTH - 110)
        self.canvas.store_canvas()

    def static_layout(self):
        self.screen.fill(DARK_GREY)  # Program background
        self.top_bar.draw_bar(self.screen)
        self.side_bar.draw_bar(self.screen)

    def dynamic_layout(self):  # This manages the option dropdown refresh
        if self.option is not None:
            if self.option == "option" and self.drop_menu.draw_menu_collision(self.mouse_cords):
                temp = self.drop_menu.draw_drop_menu(self.screen, self.mouse_cords, self.mouse_button)
                self.update_group_and_option(temp)
            elif not self.drop_menu.draw_menu_collision(self.mouse_cords):
                if self.option == "option":
                    self.option = None

    def update_group_and_option(self, input_package):
        if input_package is not None:
            input_option = input_package.split(":")
            group = input_option[0]
            option = input_option[1]

            if group == "option":
                self.group = option
                self.option = group  # The tool we use is the option
                if option != "option":
                    Button.update_icon(self.group)
            else:
                self.option = option
        self.change_tool(self.option)

    def event_manager(self):
        # Refresh mouse information
        self.refresh_mouse()
        self.canvas.update_canvas(self.screen)
        self.draw_on_canvas(self.screen)

        # Refresh canvas information
        self.canvas.store_canvas()

        # Button event
        received_package = Button.manager(self.screen, self.group, self.mouse_cords, self.mouse_button)
        self.update_group_and_option(received_package)

        self.dynamic_layout()

        for evt in event.get():
            if evt.type == QUIT:
                self.run_program = False

        # Event interruptions

    def run(self):
        while self.run_program:
            # --------------------------
            self.static_layout()
            self.event_manager()

            # --------------------------
            # time.delay(16)
            display.flip()
        font.quit()
        quit()
