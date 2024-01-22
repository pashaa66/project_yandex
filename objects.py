import math

import pygame
from level_builder import LevelBuilder

l_b = LevelBuilder()
tile_width = tile_height = 100
all_sprites = pygame.sprite.Group()
grass_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tree_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
ghost_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()
doors_group = pygame.sprite.Group()
bush_group = pygame.sprite.Group()


class Grass(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, grass_group)
        self.image = l_b.load_image('grass.jpg')
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Door(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, doors_group)
        self.image = l_b.load_image('door.png')
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Bush(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, bush_group)
        self.image = l_b.load_image('bush_with_berry.png')
        self.eaten = True
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class TreeFirst(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, tree_group)
        self.image = l_b.load_image("grass_with_tree.jpeg")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, wall_group)
        self.image = l_b.load_image("wood_wall.jpg")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, coins_group)
        self.image = l_b.load_image("coin.png")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 10))
        self.image.fill(pygame.Color('yellow'))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Ghost(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, ghost_group)
        self.image = l_b.load_image('ghost.png')
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.hp = 100
        self.speed = 2

    # def update(self,*args, **kwargs):
    #     if args:
    #         player_pos_x = 0
    #         player_pos_y = 0
    #         dx = player_pos_x - self.rect.centerx
    #         dy = player_pos_y - self.rect.centery
    #         distance = math.sqrt(dx ** 2 + dy ** 2)
    #         if distance != 0:
    #             dx = dx / distance
    #             dy = dy / distance
    #         self.rect.x += dx * self.speed
    #         self.rect.y += dy * self.speed


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, player_group)
        self.image = l_b.load_image('hero.png')
        # self.rect = self.image.get_rect().move(
        #     tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.score = 0
        self.hp = 100
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
        collided_bushes = pygame.sprite.spritecollide(self, bush_group, False)
        if collided_bushes and args and args[0] == pygame.K_e:
            for bush in collided_bushes:
                if bush.eaten:
                    self.hp += 5
                    bush.eaten = False
                    bush.image = l_b.load_image('bush.png')
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
        if pygame.sprite.spritecollide(self, ghost_group, False):
            self.hp -= 10
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
        if pygame.sprite.spritecollide(self, coins_group, True):
            self.score += 50
        if pygame.sprite.spritecollide(self, doors_group, False):
            print('a')

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullet_group.add(bullet)

    def check_alive(self):
        if self.hp <= 0:
            self.kill()
            return False
        return True


def generate_level(level):
    new_player, x, y = None, None, None
    px, py = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Grass(x, y)
            elif level[y][x] == '*':
                TreeFirst(x, y)
            elif level[y][x] == 'd':
                Door(x, y)
            elif level[y][x] == '%':
                Grass(x, y)
                Bush(x, y)
            elif level[y][x] == '~':
                Wall(x, y)
            elif level[y][x] == '#':
                Grass(x, y)
                Ghost(x, y)
            elif level[y][x] == 'C':
                Grass(x, y)
                Coin(x, y)
            elif level[y][x] == '@':
                Grass(x, y)
                px, py = x, y
    new_player = Player(px, py)
    return new_player, x, y
