import os

import pygame
import sys
from level_builder import LevelBuilder
from button import Button

pygame.init()

class EscapeFromLesok:
    def __init__(self):
        self.FPS = 50
        self.SIZE = (800, 600)
        self.WIDTH = self.SIZE[0]
        self.HEIGHT = self.SIZE[1]
        self.BLACK = pygame.Color("#000000")
        self.WHITE = pygame.Color("white")
        self.RED = pygame.Color("red")
        self.running = True
        self.button_play = Button((self.WIDTH / 2 - (252 / 2), 300), (252, 74), "Играть", "box.jpg", "grass.jpg")
        self.button_quit = Button((self.WIDTH / 2 - (252 / 2), 400), (252, 74), "Выход", "box.jpg", "grass.jpg")
        self.buttons_main_menu = [self.button_play, self.button_quit]
        self.l_b = LevelBuilder()
        self.screen = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def start_screen(self):
        intro_text = ["Побег из Леска", "",
                      "Правила игры:",
                      "Находите батарейки, чтобы фонарик не погас",
                      "Остерегайтесь темноты"]

        fon = pygame.transform.scale(self.l_b.load_image('fon.jpg'), self.SIZE)
        self.screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 0
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
                elif event.type == pygame.USEREVENT and event.button == self.button_play:
                    return

                elif event.type == pygame.USEREVENT and event.button == self.button_quit:
                    self.terminate()

                for button in self.buttons_main_menu:
                    button.handle_event(event)

            for button in self.buttons_main_menu:
                button.check_hover(pygame.mouse.get_pos())
                button.draw(self.screen)
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
            pygame.draw.line(self.screen, self.WHITE, (0, 0), (self.WIDTH, self.HEIGHT), 5)
            pygame.draw.line(self.screen, self.WHITE, (self.WIDTH, 0), (0, self.HEIGHT), 5)
            pygame.display.flip()
        self.terminate()


game = EscapeFromLesok()
game.run_game()
