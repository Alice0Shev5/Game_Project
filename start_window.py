import sys

from main import *

size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


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


def start_screen():
    pygame.init()
    pygame.display.set_caption("Magician")
    text = ['МЕНЮ',
            '',
            'Здесь будут правила игры',
            'И здесь']
    background = load_image('background.jpg')
    screen.blit(background, (0, 0))

    pygame.font.init()
    font = pygame.font.Font(None, 40)
    text_coord = 50
    for line in text:
        string = font.render(line, 1, pygame.Color('black'))
        string_rect = string.get_rect()
        text_coord = text_coord + 10
        string_rect.top = text_coord
        string_rect.x = 250
        text_coord = text_coord + string_rect.height
        screen.blit(string, string_rect)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # при нажатии на любую клавишу клавитатуры или мыши - запустится фнкция main  и начнется игра
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return main()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


start_screen()
