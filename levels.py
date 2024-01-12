import pygame
from level_builder import LevelBuilder

l_b = LevelBuilder()
tile_images = {
    'wall': l_b.load_image('box.jpg'),
    'empty': l_b.load_image('grass.jpg')
}
player_image = l_b.load_image('mar.png')
tile_width = tile_height = 50

player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Box(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites, box_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

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


class Levels:
    def __init__(self):
        pass

    def generate_level(self, level):
        new_player, x, y = None, None, None
        px, py = None, None
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile('empty', x, y)
                elif level[y][x] == '#':
                    Box('wall', x, y)
                elif level[y][x] == '@':
                    Tile('empty', x, y)
                    px, py = x, y
        new_player = Player(px, py)
        return new_player, x, y
