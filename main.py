import os

import pygame
import sys
from level_builder import LevelBuilder

pygame.init()

class EscapeFromLesok:
    def __init__(self):
        self.FPS = 50
        self.size = SIZE = WIDTH, HEIGHT = (800, 800)
        self.BLACK = pygame.Color("#000000")
        self.WHITE = pygame.Color("white")
        self.RED = pygame.Color("red")
        self.running = True
        self.l_b = LevelBuilder()
        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def start_screen(self):
        intro_text = ["Побег из Леска", "",
                      "Правила игры:",
                      "Находите батарейки, чтобы фонарик не погас",
                      "Остерегайтесь темноты"]

        fon = pygame.transform.scale(self.l_b.load_image('fon.jpg'), self.size)
        self.screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 50
        for line in intro_text:
            string_rendered = font.render(line, 1, self.RED)
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.KEYDOWN or \
                        event.type == pygame.MOUSEBUTTONDOWN:
                    return
            pygame.display.flip()
            self.clock.tick(self.FPS)

    def run_game(self):
        self.start_screen()
        while self.running:
            self.clock.tick(self.FPS)
            self.screen.fill(self.BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()
        self.terminate()


game = EscapeFromLesok()
game.run_game()
