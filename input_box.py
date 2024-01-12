import pygame


class InputBox:
    def __init__(self, pos, size, text=''):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.width = size[0]
        self.height = size[1]
        self.text = text
        self.nickname = ''
        self.COLOR_ACTIVE = pygame.Color("#FE0D00")
        self.COLOR_INACTIVE = pygame.Color("#FF4940")
        self.current_color = self.COLOR_INACTIVE
        self.active = True
        self.input_box = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.font = pygame.font.Font(None, 30)
        self.text_surface = self.font.render(self.text, True, self.current_color)
        self.is_hovered = False

    def draw(self, screen):
        self.current_color = self.COLOR_ACTIVE if self.is_hovered else self.COLOR_INACTIVE
        screen.blit(self.text_surface, (self.input_box.x + 5, self.input_box.y + 5))
        pygame.draw.rect(screen, self.current_color, self.input_box, 5)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.input_box.collidepoint(mouse_pos)

    def update_size(self):
        new_width = max(252, self.text_surface.get_width() + 10)
        self.input_box.w = new_width

    def return_nickname(self):
        return self.nickname

    def handle_event(self, event):
        if self.is_hovered:
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        self.nickname = self.text
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                    self.text_surface = self.font.render(self.text, True, self.current_color)