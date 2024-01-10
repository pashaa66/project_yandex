import os

import pygame
import sys
from level_builder import LevelBuilder
from button import Button
from input_box import InputBox

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
        self.nickname = ''
        self.running = True
        self.l_b = LevelBuilder()
        self.screen = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def main_menu(self):
        button_play = Button((self.WIDTH / 2 - (252 / 2), 200), (252, 74), "Играть", "box.jpg", "grass.jpg")
        button_rules = Button((self.WIDTH / 2 - (252 / 2), 300), (252, 74), "Правила", "box.jpg", "grass.jpg")
        button_quit = Button((self.WIDTH / 2 - (252 / 2), 400), (252, 74), "Выход", "box.jpg", "grass.jpg")
        buttons_main_menu = [button_play, button_rules, button_quit]


        while self.running:
            fon = pygame.transform.scale(self.l_b.load_image('fon.jpg'), self.SIZE)
            self.screen.blit(fon, (0, 0))
            font = pygame.font.Font(None, 50)
            text = font.render("ПОБЕГ ИЗ ЛЕСКА", 1, self.RED)
            self.screen.blit(text, (250, 50))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.USEREVENT and event.button == button_play:
                    self.login_to_the_game_menu()

                elif event.type == pygame.USEREVENT and event.button == button_rules:
                    self.rules_menu()

                elif event.type == pygame.USEREVENT and event.button == button_quit:
                    self.terminate()

                for button in buttons_main_menu:
                    button.handle_event(event)

            for button in buttons_main_menu:
                button.check_hover(pygame.mouse.get_pos())
                button.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.FPS)
    def rules_menu(self):
        button_quit_to_menu = Button((self.WIDTH / 2 - (252 / 2), 300), (252, 74), "Выход в меню", "box.jpg",
                                     "grass.jpg")
        while self.running:
            self.screen.fill(self.BLACK)
            fon = pygame.transform.scale(self.l_b.load_image('fon.jpg'), self.SIZE)
            self.screen.blit(fon, (0, 0))
            intro_text = ["Правила игры:",
                          "Находите батарейки, чтобы фонарик не погас",
                          "Остерегайтесь темноты"]
            font = pygame.font.Font(None, 36)
            text_coord = 0
            for line in intro_text:
                string_rendered = font.render(line, 1, self.RED)
                intro_rect = string_rendered.get_rect()
                text_coord += 10
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                self.screen.blit(string_rendered, intro_rect)
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.USEREVENT and event.button == button_quit_to_menu:
                    self.main_menu()
                button_quit_to_menu.handle_event(event)
            button_quit_to_menu.check_hover(pygame.mouse.get_pos())
            button_quit_to_menu.draw(self.screen)

            pygame.display.flip()
        self.terminate()

    def login_to_the_game_menu(self):
        button_quit_to_menu = Button((self.WIDTH / 2 - (252 / 2), 400), (252, 74), "Выход в меню", "box.jpg",
                                     "grass.jpg")
        nickname_input_box = InputBox((self.WIDTH / 2 - (252 / 2), 250), (252, 74))

        while self.running:
            self.screen.fill(self.BLACK)
            fon = pygame.transform.scale(self.l_b.load_image('fon.jpg'), self.SIZE)
            self.screen.blit(fon, (0, 0))
            font = pygame.font.Font(None, 50)
            text = font.render("Введите ваш никнейм", 1, self.RED)
            self.screen.blit(text, (220, 200))
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.USEREVENT and event.button == button_quit_to_menu:
                    self.main_menu()
                button_quit_to_menu.handle_event(event)
            nickname_input_box.draw(self.screen)
            nickname_input_box.check_hover(pygame.mouse.get_pos())
            button_quit_to_menu.check_hover(pygame.mouse.get_pos())
            button_quit_to_menu.draw(self.screen)
            pygame.display.flip()
        self.terminate()


    def run_game(self):
        self.main_menu()
        while self.running:
            self.clock.tick(self.FPS)
            self.screen.fill(self.BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            fon = pygame.transform.scale(self.l_b.load_image('fon.jpg'), self.SIZE)
            self.screen.blit(fon, (0, 0))
            pygame.display.flip()
        self.terminate()


game = EscapeFromLesok()
game.run_game()
