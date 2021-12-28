from sys import platform
from pygame import font, display, FULLSCREEN, mouse, time, event, QUIT
from elements import Button
from static import Icons


class Canvas:
    def __init__(self):
        self.mouse_x, self.mouse_y, self.mouse_b = 0, 0, 0

        self.run_program = True
        font.init()

        display.set_caption("Simply Paint")
        self.program_font = font.SysFont("courier", 12)
        self.screen = display.set_mode((1280, 720))  # 1440 900
        self.screen.fill((200, 200, 200))

        # Test
        Button("pencil", Icons.PENCIL, 100, 10,)
        Button("brush", Icons.BRUSH, 200, 10)

    def event_manager(self):
        self.mouse_x, self.mouse_y = mouse.get_pos()
        self.mouse_b = mouse.get_pressed()

        for evt in event.get():
            if evt.type == QUIT:
                self.run_program = False

    def run(self):
        while self.run_program:
            self.event_manager()

            a = Button.manager(self.screen, self.mouse_x, self.mouse_y, self.mouse_b )
            if a is not None:
                print(a)

            time.delay(16)
            display.flip()
        font.quit()
        del self.program_font
        quit()
