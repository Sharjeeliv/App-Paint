from pygame import font, display, mouse, time, event, QUIT
from .elements import Button, DropMenu
from .graphic_elements.canvas import Canvas
from .graphic_elements.bars import Bar
from .colours import *
from .tools import *

'''
The stage module is responsible for "staging" the app/game and hence is usually
present in all programs. It's primary responsibilities are to control the flow (direct the play),
and layout the gui (set the stage).
'''


class Stage:
    _state = pencil.Pencil()

    def __init__(self):
        # Initialize variables
        self.mouse_x, self.mouse_y, self.mouse_b = 0, 0, 0
        self.prev_mouse_x, self.prev_mouse_y = 0, 0
        self.WINDOW_LENGTH, self.WINDOW_WIDTH = 1280, 720
        self.run_program = True

        # Program state variables
        self.group, self.option, self.canvas = "draw", None, None

        # Initialize font
        font.init()
        self.program_font = font.SysFont("courier", 12)

        # Initialize screen
        display.set_caption("Simply Paint")
        self.screen = display.set_mode((self.WINDOW_LENGTH, self.WINDOW_WIDTH))

        # Program setup
        self.drop_menu = DropMenu(5, 5, 90, 630)

        self.static_layout()
        self.canvas = Canvas(self.screen, 10, 110, self.WINDOW_LENGTH - 80, self.WINDOW_WIDTH - 110)
        self.canvas.store_canvas()

    def static_layout(self):  # Used for init as well
        # Back screen & Canvas
        self.screen.fill(DARK_GREY)

        # Bar Elements
        top_bar = Bar(self.WINDOW_LENGTH, 100)
        top_bar.draw_bar(self.screen)
        side_bar = Bar(100, self.WINDOW_WIDTH, self.WINDOW_LENGTH - 60)
        side_bar.draw_bar(self.screen)

    def dynamic_layout(self):  # This manages the option dropdown refresh
        if self.option is not None:
            if self.option == "option" and self.drop_menu.draw_menu_collision(self.mouse_x, self.mouse_y):
                temp = self.drop_menu.draw_drop_menu(self.screen, self.mouse_x, self.mouse_y, self.mouse_b)
                self.update_group_and_option(temp)
            elif not self.drop_menu.draw_menu_collision(self.mouse_x, self.mouse_y):
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
        # print("option is ", self.option)

    def event_manager(self):
        # Refresh mouse information
        self.prev_mouse_x, self.prev_mouse_y = self.mouse_x, self.mouse_y
        self.mouse_x, self.mouse_y = mouse.get_pos()
        self.mouse_b = mouse.get_pressed()

        self.canvas.update_canvas(self.screen)
        if self.mouse_b[0] == 1 and self.canvas.on_canvas((self.mouse_x, self.mouse_y)):
            print('active buttons')
            self._state.draw_to_screen(self.screen, self.mouse_x, self.mouse_y, self.prev_mouse_x, self.prev_mouse_y)

        # Refresh canvas information

        self.canvas.store_canvas()

        # Button event
        received_package = Button.manager(self.screen, self.group, self.mouse_x, self.mouse_y, self.mouse_b)
        self.update_group_and_option(received_package)

        self.dynamic_layout()

        # Event interruptions
        for evt in event.get():
            if evt.type == QUIT:
                self.run_program = False

    def run(self):
        while self.run_program:
            # --------------------------
            self.static_layout()
            self.event_manager()

            # --------------------------
            # time.delay(16)
            display.flip()
        font.quit()
        del self.program_font
        quit()
