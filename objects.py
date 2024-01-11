import pygame
from level_builder import LevelBuilder


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.l_b = LevelBuilder()
        self.image = self.l_b.load_image("grass.jpg")
        self.tile_width = 50
        self.tile_height = 50
        self.rect = self.image.get_rect().move(
            self.tile_width * pos_x, self.tile_height * pos_y)


class Box(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites, box_group)
        self.l_b = LevelBuilder()
        self.image = self.l_b.load_image("box.jpg")
        self.tile_width = 50
        self.tile_height = 50
        self.rect = self.image.get_rect().move(
            self.tile_width * pos_x, self.tile_height * pos_y)