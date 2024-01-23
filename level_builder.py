import os
import sys
import pygame

class LevelBuilder:
    def __init__(self):
        pass

    def load_level(self, filename):
        try:
            filename = "data/" + filename
            with open(filename, 'r') as mapFile:
                level_map = [line.strip() for line in mapFile]
                max_width = max(map(len, level_map))
            return list(map(lambda x: x.ljust(max_width, '.'), level_map))
        except FileNotFoundError as e:
            print(e)

    def load_image(self, name, color_key=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if color_key is not None:
            image = image.convert()
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
        else:
            image = image.convert_alpha()
        return image

    def terminate(self):
        pygame.quit()
        sys.exit()

    def clear_sprites(self, group):
        for sprite in group:
            sprite.kill()
