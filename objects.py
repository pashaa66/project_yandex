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
# ghost_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()
doors_group = pygame.sprite.Group()
bush_group = pygame.sprite.Group()
floor_group = pygame.sprite.Group()
keys_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
furniture_group = pygame.sprite.Group()
holes_group = pygame.sprite.Group()
boxes_group = pygame.sprite.Group()

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1080


class Grass(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, designation):
        super().__init__(all_sprites, grass_group)
        if designation == ".":
            self.image = l_b.load_image("grass.jpg")
        elif designation == ",":
            self.image = l_b.load_image("grass2.jpg")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Candle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, furniture_group)
        self.image = l_b.load_image("candle.png")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Hole(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, holes_group)
        self.image = l_b.load_image("hole.png")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Box(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, boxes_group)
        self.image = l_b.load_image("box.png")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Floor(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, floor_group)
        self.image = l_b.load_image("floor.jpg")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Door(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, doors_group)
        self.image = l_b.load_image("door.png")
        self.is_close = True
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Bed(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, furniture_group)
        self.image = l_b.load_image("bed.jpg", color_key=-1)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Bush(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, bush_group)
        self.image = l_b.load_image("bush_with_berry.png")
        self.eaten = True
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, designation):
        super().__init__(all_sprites, tree_group)
        if designation == "*":
            self.image = l_b.load_image("tree2.jpg")
        elif designation == "+":
            self.image = l_b.load_image("grass2_with_tree2.jpeg")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Key(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, keys_group)
        self.image = l_b.load_image("key.png")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 20, tile_height * pos_y + 15)


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
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = l_b.load_image("bullet.jpg")
        if direction == pygame.K_UP:
            self.speedx = 0
            self.speedy = -10
            self.image = l_b.load_image("bullet.jpg")
        elif direction == pygame.K_DOWN:
            self.speedx = 0
            self.speedy = 10
            self.image = l_b.load_image("bullet2.jpg")
        elif direction == pygame.K_LEFT:
            self.speedx = -10
            self.speedy = 0
            self.image = l_b.load_image("bullet4.jpg")
        elif direction == pygame.K_RIGHT:
            self.speedx = 10
            self.speedy = 0
            self.image = l_b.load_image("bullet3.jpg")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()


class Skeleton(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, enemy_group)
        self.image = l_b.load_image("skeleton.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.hp = 75
        self.speed = 2


class Ghost(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, enemy_group)
        self.image = l_b.load_image("ghost.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        self.hp = 75
        self.speed = 2

    # def move_G(self):
    #     dx = SCREEN_WIDTH - self.rect.centerx
    #     dy = SCREEN_HEIGHT - self.rect.centery
    #     distance = math.sqrt(dx ** 2 + dy ** 2)
    #     if distance != 0:
    #         dx = dx / distance
    #         dy = dy / distance
    #     self.rect.x += dx * self.speed
    #     self.rect.y += dy * self.speed


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(all_sprites, player_group)
        self.image = l_b.load_image("hero.png")
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.score = 0
        self.hp = 100
        self.key = False
        self.speed_x = 0
        self.speed_y = 0
        self.eaten = 0
        self.speed = 50

    def update(self, *args, **kwargs):
        self.speed_x = 0
        self.speed_y = 0
        if args:
            if args[0] == pygame.K_w:
                self.speed_y = -self.speed
            if args[0] == pygame.K_s:
                self.speed_y = self.speed
            if args[0] == pygame.K_a:
                self.speed_x = -self.speed
                self.image = l_b.load_image("hero2.png")
            if args[0] == pygame.K_d:
                self.speed_x = self.speed
                self.image = l_b.load_image("hero.png")
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        collided_bushes = pygame.sprite.spritecollide(self, bush_group, False)
        if collided_bushes and args and args[0] == pygame.K_e:
            for bush in collided_bushes:
                if bush.eaten:
                    self.hp += 5
                    bush.eaten = False
                    self.eaten += 1
                    bush.image = l_b.load_image("bush.png")
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
        if pygame.sprite.spritecollide(self, boxes_group, False):
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
        if pygame.sprite.spritecollide(self, enemy_group, False):
            self.hp -= 25
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
        collided_doors = pygame.sprite.spritecollide(self, doors_group, False)
        if collided_doors and args and args[0] == pygame.K_e:
            for door in collided_doors:
                if door.is_close:
                    if not self.key:
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
                    else:
                        door.is_close = False
                        self.key = False
                        door.kill()

        if pygame.sprite.spritecollide(self, coins_group, True):
            self.score += 50
        if pygame.sprite.spritecollide(self, keys_group, True):
            self.key = True

    def shoot(self, key):
        print(key)
        bullet = Bullet(self.rect.centerx, self.rect.top, key)
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
                Grass(x, y, ".")
            elif level[y][x] == ',':
                Grass(x, y, ",")
            elif level[y][x] == '!':
                Grass(x, y, ",")
                Candle(x, y)
            elif level[y][x] == '^':
                Floor(x, y)
                Candle(x, y)
            elif level[y][x] == '*':
                Grass(x, y, ".")
                Tree(x, y, "*")
            elif level[y][x] == "+":
                Tree(x, y, "+")
            elif level[y][x] == 'd':
                Floor(x, y)
                Door(x, y)
            elif level[y][x] == '%':
                Grass(x, y, ".")
                Bush(x, y)
            elif level[y][x] == '~':
                Wall(x, y)
            elif level[y][x] == '#':
                Grass(x, y, ".")
                Ghost(x, y)
            elif level[y][x] == 'f':
                Floor(x, y)
            elif level[y][x] == 'k':
                Grass(x, y, ".")
                Key(x, y)
                Ghost(x, y)
            elif level[y][x] == 'C':
                Grass(x, y, ".")
                Coin(x, y)
            elif level[y][x] == 'c':
                Floor(x, y)
                Coin(x, y)
            elif level[y][x] == 'i':
                Grass(x, y, ',')
                Coin(x, y)
            elif level[y][x] == 's':
                Grass(x, y, ",")
                Skeleton(x, y)
            elif level[y][x] == 'z':
                Floor(x, y)
                Bed(x, y)
            elif level[y][x] == 'h':
                Grass(x, y, ',')
                Hole(x, y)
            elif level[y][x] == 'x':
                Floor(x, y)
                Box(x, y)
            elif level[y][x] == 'X':
                Floor(x, y)
                Key(x, y)
                Box(x, y)
            elif level[y][x] == '@':
                Grass(x, y, ".")
                px, py = x, y
    new_player = Player(px, py)
    return new_player, x, y
