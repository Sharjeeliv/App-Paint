
class Slider:

    def __init__(self, icon, position):
        self.position = position
        self.width, self.height = icon.get_size()
        self.icon = icon

    def draw_slider(self, screen):
        screen.blit(self.icon, self.position)