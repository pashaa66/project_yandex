import pygame
from level_builder import LevelBuilder

class Button:
    def __init__(self, pos, size, text, image, hover_image=None):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.BLACK = pygame.Color("black")
        self.width = size[0]
        self.height = size[1]
        self.image = image
        self.text = text
        self.level_builder = LevelBuilder()
        self.img = self.level_builder.load_image(self.image)
        self.img = pygame.transform.scale(self.img, (size[0], size[1]))
        if hover_image:
            self.hover_image = self.level_builder.load_image(hover_image)
            self.hover_image = pygame.transform.scale(self.hover_image, (size[0], size[1]))
        self.rect = self.img.get_rect(topleft=(pos[0], pos[1]))
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.img
        screen.blit(current_image, self.rect.topleft)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, self.BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


