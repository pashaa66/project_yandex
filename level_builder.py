import os
import sys
import pygame

class LevelBuilder:
    def __init__(self):
        self.filename = "map.txt"

    def load_level(self):
        try:
            filename = "data/" + self.filename
            with open(filename, 'r') as mapFile:
                level_map = [line.strip() for line in mapFile]
                max_width = max(map(len, level_map))
            return list(map(lambda x: x.ljust(max_width, '.'), level_map))
        except FileNotFoundError as e:
            print(e)

    def load_image(self, name):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        return image