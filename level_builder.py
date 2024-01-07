import os
import sys
import pygame



class LevelBuilder:
    def __init__(self):
        self.filename = 'map.txt'

    def load_level(self):
        try:
            filename = "data/" + self.filename
            with open(filename, 'r') as mapFile:
                level_map = [line.strip() for line in mapFile]
                max_width = max(map(len, level_map))
            return list(map(lambda x: x.ljust(max_width, '.'), level_map))
        except FileNotFoundError as e:
            print(e)

    def load_image(self, name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        # if colorkey is not None:
        #     image = image.convert()
        #     if colorkey == -1:
        #         colorkey = image.get_at((0, 0))
        #     image.set_colorkey(colorkey)
        # else:
        #     image = image.convert_alpha()
        return image

