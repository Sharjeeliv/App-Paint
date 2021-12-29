from pygame import font, display, mouse, time, event, QUIT
from elements import Button, Canvas, Bar
from static import Icons
from colours import *

'''
The stage module is responsible for "staging" the app/game and hence is usually
present in all programs. It's primary responsibilities are to control the flow,
initialize, and layout the gui.
'''


class Stage:
    def __init__(self):
        # Initialize variables
        self.canvas = None
        self.mouse_x, self.mouse_y, self.mouse_b = 0, 0, 0
        self.WINDOW_LENGTH, self.WINDOW_WIDTH = 1280, 720
        self.run_program = True

        # Initialize font
        font.init()
        self.program_font = font.SysFont("courier", 12)

        # Initialize screen
        display.set_caption("Simply Paint")
        self.screen = display.set_mode((self.WINDOW_LENGTH, self.WINDOW_WIDTH))

        # Program setup
        self.current_option = 'draw'
        self.static_layout()

    def static_layout(self): # Used for init as well

        # Back screen & Canvas
        self.screen.fill(DARK_GREY)
        self.canvas = Canvas(self.screen, 10, 110, self.WINDOW_LENGTH - 80, self.WINDOW_WIDTH - 110)

        # Bar Elements
        top_bar = Bar(self.WINDOW_LENGTH, 100)
        side_bar = Bar(100, self.WINDOW_WIDTH, self.WINDOW_LENGTH - 60)
        top_bar.draw_bar(self.screen)
        side_bar.draw_bar(self.screen)

        # Test

        Button("option:draw", Icons.DRAW, 10, 10)
        Button("draw:pencil", Icons.PENCIL, 100, 10)
        Button("draw:marker", Icons.MARKER, 190, 10)
        Button("draw:fount_pen", Icons.FOUNT_PEN, 280, 10)

        Button("option:paint", Icons.DRAW, 10, 10)
        Button("paint:brush", Icons.BRUSH, 100, 10)
        Button("paint:spray", Icons.SPRAY, 190, 10)

        Button("option:erase", Icons.ERASE, 10, 10)
        Button("erase:eraser", Icons.ERASER, 100, 10)
        Button("erase:clear", Icons.CLEAR, 190, 10)

        Button("option:shapes", Icons.SHAPES, 10, 10)
        Button("shapes:circle", Icons.CIRCLE, 100, 10)
        Button("shapes:square", Icons.SQUARE, 190, 10)
        Button("shapes:line", Icons.LINE, 280, 10)
        Button("shapes:ellipse", Icons.ELLIPSE, 370, 10)

        Button("option:stamps", Icons.STAMPS, 10, 10)
        Button("option:stamp_1", Icons.STAMP_1, 100, 10)
        Button("option:stamp_2", Icons.STAMP_2, 190, 10)
        Button("option:stamp_3", Icons.STAMP_3, 280, 10)
        Button("option:stamp_4", Icons.STAMP_4, 370, 10)
        Button("option:stamp_6", Icons.STAMP_6, 460, 10)

        Button("option:settings", Icons.SETTINGS, 10, 10)
        Button("option:exit", Icons.EXIT, 100, 10)

    def dynamic_layout(self):
        pass

    def event_manager(self):
        self.mouse_x, self.mouse_y = mouse.get_pos()
        self.mouse_b = mouse.get_pressed()

        self.canvas.store_canvas()
        self.canvas.update_canvas(self.screen)

        tool = Button.manager(self.screen, self.current_option, self.mouse_x, self.mouse_y, self.mouse_b)

        for evt in event.get():
            if evt.type == QUIT:
                self.run_program = False

    def run(self):
        while self.run_program:
            # --------------------------
            self.event_manager()

            # --------------------------
            time.delay(16)
            display.flip()
        font.quit()
        del self.program_font
        quit()
