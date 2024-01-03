import os

import pygame
import sys

pygame.init()
BLACK = pygame.Color("#000000")
SIZE = WIDTH, HEIGHT = (550, 550)
FPS = 50
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()

running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
terminate()