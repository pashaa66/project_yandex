import pygame
from level_builder import LevelBuilder
l_b = LevelBuilder()
tile_width = tile_height = 100
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tree_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()
ls = [tree_group, wall_group]

class Grass(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = l_b.load_image('grass.jpg')
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class TreeFirst(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y):
        super().__init__(tree_group, all_sprites)
        self.image = l_b.load_image("grass_with_tree.jpeg")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
class Wall(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y):
        super().__init__(wall_group, all_sprites)
        self.image = l_b.load_image("wood_wall.jpg")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
class Ghost(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(ghost_group, all_sprites)
        self.image = l_b.load_image('ghost.png')
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = l_b.load_image('hero.png')
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.speed_x = 0
        self.speed_y = 0
        self.speed = 50

    def update(self, *args, **kwargs):
        self.speed_x = 0
        self.speed_y = 0
        if args:
            if args[0] == pygame.K_w:
                # self.rect = self.rect.move(0, -50)
                self.speed_y = -self.speed
            if args[0] == pygame.K_s:
                # self.rect = self.rect.move(0, 50)
                self.speed_y = self.speed
            if args[0] == pygame.K_a:
                # self.rect = self.rect.move(-50, 0)
                self.speed_x = -self.speed
                self.image = l_b.load_image('hero2.png')
            if args[0] == pygame.K_d:
                # self.rect = self.rect.move(50, 0)
                self.speed_x = self.speed
                self.image = l_b.load_image('hero.png')
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        if pygame.sprite.spritecollide(self, tree_group, False):
            if args[0] == pygame.K_w:
                self.speed_y = self.speed
            if args[0] == pygame.K_s:
                self.speed_y = -self.speed
            if args[0] == pygame.K_a:
                self.speed_x = self.speed
            if args[0] == pygame.K_d:
                self.speed_x = -self.speed
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        if pygame.sprite.spritecollide(self, wall_group, False):
            if args[0] == pygame.K_w:
                self.speed_y = self.speed
            if args[0] == pygame.K_s:
                self.speed_y = -self.speed
            if args[0] == pygame.K_a:
                self.speed_x = self.speed
            if args[0] == pygame.K_d:
                self.speed_x = -self.speed
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y


def generate_level(level):
    new_player, x, y = None, None, None
    px, py = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Grass(x, y)
            elif level[y][x] == '*':
                TreeFirst(x, y)
            elif level[y][x] == '~':
                Wall(x, y)
            elif level[y][x] == '#':
                Grass(x,y)
                Ghost(x, y)
            elif level[y][x] == '@':
                Grass(x, y)
                px, py = x, y
    new_player = Player(px, py)
    return new_player, x, y