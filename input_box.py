import pygame

class InputBox:
    def __init__(self, pos, size, text=''):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.text = text
        self.COLOR_ACTIVE = pygame.Color("#FE0D00")
        self.COLOR_INACTIVE = pygame.Color("#FF4940")
        self.color = self.COLOR_INACTIVE
        self.active = False
        self.input_box = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.font = pygame.font.Font(None, 30)
        self.text_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.text_surface, (self.input_box.x + 5, self.input_box.y + 5))
        pygame.draw.rect(screen, self.color, self.input_box, 2)







