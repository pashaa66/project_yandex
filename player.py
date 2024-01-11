import pygame
from level_builder import LevelBuilder

player_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.l_b = LevelBuilder()
        self.tile_width = 50
        self.tile_height = 50
        self.image = self.l_b.load_image("mar.phg")
        self.rect = self.image.get_rect().move(
            self.tile_width * pos_x + 15, self.tile_height * pos_y + 5)

    def update(self, *args, **kwargs):
        if args:
            if args[0] == pygame.K_UP:
                self.rect = self.rect.move(0, -50)
            if args[0] == pygame.K_DOWN:
                self.rect = self.rect.move(0, 50)
            if args[0] == pygame.K_LEFT:
                self.rect = self.rect.move(-50, 0)
            if args[0] == pygame.K_RIGHT:
                self.rect = self.rect.move(50, 0)
        if pygame.sprite.spritecollide(self, box_group, False):
            if args[0] == pygame.K_UP:
                self.rect = self.rect.move(0, 50)
            if args[0] == pygame.K_DOWN:
                self.rect = self.rect.move(0, -50)
            if args[0] == pygame.K_LEFT:
                self.rect = self.rect.move(50, 0)
            if args[0] == pygame.K_RIGHT:
                self.rect = self.rect.move(-50, 0)