from pygame import font, display, mouse, time, event, QUIT
from elements import Button, Canvas
from static import Icons, Colours


class Stage:
    def __init__(self):
        self.mouse_x, self.mouse_y, self.mouse_b = 0, 0, 0
        self.WINDOW_LENGTH, self.WINDOW_WIDTH = 1280, 720
        self.run_program = True

        font.init()
        self.program_font = font.SysFont("courier", 12)

        display.set_caption("Simply Paint")
        self.screen = display.set_mode((self.WINDOW_LENGTH, self.WINDOW_WIDTH))  # 1440 900
        self.screen.fill(Colours.LIGHT_GREY)

        # Test
        Button("pencil", Icons.PENCIL, 100, 10)
        Button("brush", Icons.BRUSH, 200, 10)

        self.canvas = Canvas(self.screen, 10, 110, 200, 200)

    def static_layout(self):
        pass

    def dynamic_layout(self):
        pass

    def event_manager(self):
        self.mouse_x, self.mouse_y = mouse.get_pos()
        self.mouse_b = mouse.get_pressed()

        tool = Button.manager(self.screen, self.mouse_x, self.mouse_y, self.mouse_b)

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