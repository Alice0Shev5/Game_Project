import os
import sys
import pygame


def load_image(name):
    fullname = 'data' + '/' + name
    try:
        if name[-2:] == 'jpg':
            image = pygame.image.load(fullname).convert()
        else:
            image = pygame.image.load(fullname).convert_alpha()
    except:
        print('Cannot load image:', name)
        raise SystemExit
    return image


def load_image2(name, colorkey=None):  # на всякий пажарный, пусть будет
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


screen_width = 800  # setting
screen_height = 600  # setting
FPS = 30
size = [screen_width, screen_height]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
background = load_image('background.jpg')
back = pygame.image.load('data/bg.jpg')





