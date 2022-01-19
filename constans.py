# в этом файле находятся те функции и переменные, которые используются в игре несколько раз и не меняются
import os
import sys

import pygame

size = width, height = (550, 550)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
fire_group = pygame.sprite.Group()
trap_group = pygame.sprite.Group()
star_group = pygame.sprite.Group()
# функции для загрузки всех изображений игры


def load_image2(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_image(name):
    fullname = 'data' + '/' + name
    try:
        if name[-2:] == 'jpg':
            image = pygame.image.load(fullname).convert()
        else:
            image = pygame.image.load(fullname).convert_alpha()
    except:
        print('Невозможно загрузить изображение:', name)
        raise SystemExit()

    return image
