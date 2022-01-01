from pygame import font, display, mouse, time, event, QUIT
from elements import Button, Canvas, Bar, DropMenu
from static import *
from colours import *

'''
The stage module is responsible for "staging" the app/game and hence is usually
present in all programs. It's primary responsibilities are to control the flow,
initialize, and layout the gui.
'''


class Stage:
    def __init__(self):
        # Initialize variables
        self.mouse_x, self.mouse_y, self.mouse_b = 0, 0, 0
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
        self.initial_layout()

    @staticmethod
    def initial_layout():
        Button("option:general", DRAW, 10, 10)

        Button("draw:pencil", PENCIL, 100, 10)
        Button("draw:marker", MARKER, 190, 10)
        Button("draw:fount_pen", FOUNT_PEN, 280, 10)

        Button("paint:brush", BRUSH, 100, 10)
        Button("paint:spray", SPRAY, 190, 10)

        Button("erase:eraser", ERASER, 100, 10)
        Button("erase:clear", CLEAR, 190, 10)

        Button("shapes:circle", CIRCLE, 100, 10)
        Button("shapes:square", SQUARE, 190, 10)
        Button("shapes:line", LINE, 280, 10)
        Button("shapes:ellipse", ELLIPSE, 370, 10)

        Button("stamps:stamp_1", STAMP_1, 100, 10)
        Button("stamps:stamp_2", STAMP_2, 190, 10)
        Button("stamps:stamp_3", STAMP_3, 280, 10)
        Button("stamps:stamp_4", STAMP_4, 370, 10)
        Button("stamps:stamp_6", STAMP_6, 460, 10)

        Button("settings:exit", EXIT, 100, 10)

        Button("option:draw", DRAW, 10, 100)
        Button("option:paint", PAINT, 10, 190)
        Button("option:erase", ERASE, 10, 280)
        Button("option:shapes", SHAPES, 10, 370)
        Button("option:stamps", STAMPS, 10, 460)
        Button("option:settings", SETTINGS, 10, 550)

        Button("static:load", LOAD, 1226, 10, 48, 48)
        Button("static:save", SAVE, 1226, 68, 48, 48)
        Button("static:redo", REDO, 1226, 126, 48, 48)
        Button("static:undo", UNDO, 1226, 184, 48, 48)

        Button("static:colour", COLOUR, 1226, 242, 48, 48)
        Button("static:opacity", OPACITY, 1226, 300, 48, 48)
        Button("static:width", WIDTH, 1226, 358, 48, 48)

    def static_layout(self):  # Used for init as well
        # Back screen & Canvas
        self.screen.fill(DARK_GREY)
        self.canvas = Canvas(self.screen, 10, 110, self.WINDOW_LENGTH - 80, self.WINDOW_WIDTH - 110)

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

    def event_manager(self):
        # Refresh mouse information
        self.mouse_x, self.mouse_y = mouse.get_pos()
        self.mouse_b = mouse.get_pressed()

        # Refresh canvas information
        self.canvas.store_canvas()
        self.canvas.update_canvas(self.screen)

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
            time.delay(16)
            display.flip()
        font.quit()
        del self.program_font
        quit()
