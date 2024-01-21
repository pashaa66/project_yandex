import sys

from button import Button
from input_box import InputBox
from database import DataBase
from camera import Camera
from objects import *
import pygame
from level_builder import LevelBuilder

pygame.init()


class EscapeFromForest:
    def __init__(self):
        self.FPS = 60
        self.SIZE = (1080, 720)
        self.WIDTH = self.SIZE[0]
        self.HEIGHT = self.SIZE[1]
        self.BLACK = pygame.Color("#000000")
        self.WHITE = pygame.Color("white")
        self.RED = pygame.Color("red")
        self.nickname = ''
        self.db = DataBase()
        self.score = 0
        self.camera = Camera(self.WIDTH, self.HEIGHT)
        self.running = True
        self.l_b = LevelBuilder()
        self.screen = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def main_menu(self):
        button_play = Button((self.WIDTH / 2 - (252 / 2), 200), (252, 100), "Играть", "button_1.jpg", "button_2.jpg")
        button_rules = Button((self.WIDTH / 2 - (252 / 2), 300), (252, 100), "Правила", "button_1.jpg", "button_2.jpg")
        button_quit = Button((self.WIDTH / 2 - (252 / 2), 400), (252, 100), "Выход", "button_1.jpg", "button_2.jpg")
        buttons_main_menu = [button_play, button_rules, button_quit]

        while self.running:
            fon = pygame.transform.scale(self.l_b.load_image('fon.jpg'), self.SIZE)
            self.screen.blit(fon, (0, 0))
            font = pygame.font.Font(None, 50)
            text = font.render("ПОБЕГ ИЗ ЛЕСКА", 1, self.RED)
            self.screen.blit(text, (self.WIDTH / 2 - (252 / 2) - 20, 50))

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
        button_quit_to_menu = Button((self.WIDTH / 2 - (252 / 2), 300), (252, 100), "Выход в меню", "button_1.jpg",
                                     "button_2.jpg")
        while self.running:
            self.screen.fill(self.BLACK)
            fon = pygame.transform.scale(self.l_b.load_image('fon.jpg'), self.SIZE)
            self.screen.blit(fon, (0, 0))
            intro_text = ["Правила игры:",
                          "Зарабатывайте очки, собирая монетки",
                          "Остерегайтесь темноты", "Находите оружие на земле",
                          "Чтобы поговорить с персонажем, нажмите 'E'"]
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
        button_quit_to_menu = Button((self.WIDTH / 2 - (252 / 2), 400), (252, 100), "Выход в меню", "button_1.jpg",
                                     "button_2.jpg")
        button_login = Button((self.WIDTH / 2 - (252 / 2), 320), (252, 100), "Играть", "button_1.jpg",
                              "button_2.jpg")
        nickname_input_box = InputBox((self.WIDTH / 2 - (252 / 2), 250), (252, 74))
        buttons = [button_login, button_quit_to_menu]

        while self.running:
            self.screen.fill(self.BLACK)
            fon = pygame.transform.scale(self.l_b.load_image('fon.jpg'), self.SIZE)
            self.screen.blit(fon, (0, 0))
            font = pygame.font.Font(None, 50)
            text = font.render("Введите ваш никнейм", 1, self.RED)
            self.screen.blit(text, (self.WIDTH / 2 - (252 / 2) - 40, 200))
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.USEREVENT and event.button == button_quit_to_menu:
                    self.main_menu()
                elif event.type == pygame.USEREVENT and event.button == button_login:
                    self.nickname = nickname_input_box.return_nickname()
                    check_nickname = self.db.check_nickname(self.nickname)
                    if check_nickname == 'OK':
                        self.run_game()
                    else:
                        print(check_nickname)

                nickname_input_box.handle_event(event)

                for button in buttons:
                    button.handle_event(event)

            for button in buttons:
                button.check_hover(pygame.mouse.get_pos())
                button.draw(self.screen)
            nickname_input_box.update_size()

            nickname_input_box.draw(self.screen)
            nickname_input_box.check_hover(pygame.mouse.get_pos())

            pygame.display.flip()
        self.terminate()

    def run_game(self):
        player, level_x, level_y = generate_level(self.l_b.load_level())
        while self.running:
            self.screen.fill(self.BLACK)
            fon = pygame.transform.scale(self.l_b.load_image('fon.jpg'), self.SIZE)
            self.screen.blit(fon, (0, 0))
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    player.update(event.key)
                    player.check_alive()
                    self.score = player.score
                    if event.key == pygame.K_SPACE:
                        player.shoot()
            # for ghost in ghost_group:
            #     ghost.update(player_pos)
            all_sprites.update()
            self.camera.update(player)
            for sprite in all_sprites:
                self.camera.apply(sprite)
            all_sprites.draw(self.screen)
            pygame.display.flip()
        self.terminate()


game = EscapeFromForest()
game.run_game()
