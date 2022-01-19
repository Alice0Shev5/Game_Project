import os

import pygame
import sys

pygame.init()
# все для музыки
pygame.mixer.music.load("music/msc2.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.09)
stop_music = True


def music():
    global stop_music
    if stop_music:
        stop_music = False
        pygame.mixer.music.pause()
    else:
        stop_music = True
        pygame.mixer.music.unpause()


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


def terminate():
    pygame.quit()
    sys.exit()


def level_1():
    player, level_x, level_y, fire, trap = generate_level(load_level("level_1.txt"))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                player.move_up()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                player.move_down()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                player.move_left()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                player.move_right()

            if event.type == pygame.QUIT:
                terminate()

            if player.rect.right > 550:
                player.rect.right = 550

            if player.rect.left < 0:
                player.rect.left = 0

            if pygame.sprite.collide_rect(player, trap):
                final_screen()

            if not pygame.sprite.collide_rect(player, fire):
                screen.fill(pygame.Color(0, 0, 0))
                tiles_group.draw(screen)
                player_group.draw(screen)
                fire_group.draw(screen)
                trap_group.draw(screen)
            else:
                all_sprites.empty()
                player_group.empty()
                tiles_group.empty()
                fire_group.empty()
                trap_group.empty()

                return

        pygame.display.flip()
        clock.tick(FPS)


def level_2():
    player, level_x, level_y, fire, trap = generate_level(load_level("level_2.txt"))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                player.move_up()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                player.move_down()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                player.move_left()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                player.move_right()
            if event.type == pygame.QUIT:
                terminate()

        if player.rect.right > 550:
            player.rect.right = 550

        if player.rect.left < 0:
            player.rect.left = 0

        for el in trap_group:
            if pygame.sprite.collide_rect(player, el):
                final_screen()

        if not pygame.sprite.collide_rect(player, fire):
            screen.fill(pygame.Color(0, 0, 0))
            tiles_group.draw(screen)
            player_group.draw(screen)
            fire_group.draw(screen)
            trap_group.draw(screen)
        else:
            all_sprites.empty()
            player_group.empty()
            tiles_group.empty()
            fire_group.empty()
            trap_group.empty()
            return

        pygame.display.flip()
        clock.tick(FPS)


def level_3():
    player, level_x, level_y, fire, trap = generate_level(load_level("level_3.txt"))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                player.move_up()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                player.move_down()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                player.move_left()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                player.move_right()

            if event.type == pygame.QUIT:
                terminate()

        if player.rect.right > 550:
            player.rect.right = 550

        if player.rect.left < 0:
            player.rect.left = 0

        for el in trap_group:
            if pygame.sprite.collide_rect(player, el):
                final_screen()

        if not pygame.sprite.collide_rect(player, fire):
            screen.fill(pygame.Color(0, 0, 0))
            tiles_group.draw(screen)
            player_group.draw(screen)
            fire_group.draw(screen)
            trap_group.draw(screen)
        else:
            all_sprites.empty()
            player_group.empty()
            tiles_group.empty()
            fire_group.empty()
            trap_group.empty()
            final_screen()

        pygame.display.flip()
        clock.tick(FPS)


def start_screen():
    background = load_image('background.jpg')
    screen.blit(background, (0, 0))

    pygame.font.init()
    font = pygame.font.Font(None, 40)
    # Надписи и эллипсы
    text = {'Map': [130, 190, 250, 200], 'Help': [130, 270, 250, 280],
            'Music': [130, 350, 240, 360], 'Exit': [130, 430, 255, 440]}
    for key, zn in text.items():
        if key == 'Exit':
            pygame.draw.ellipse(screen, (60, 50, 230), (130, 430, 300, 50))
        else:
            pygame.draw.ellipse(screen, (100, 100, 230), (zn[0], zn[1], 300, 50))
        string = font.render(key, 1, (255, 255, 255))
        screen.blit(string, (zn[2], zn[3]))
    string = pygame.font.Font(None, 60).render('M a g i c a i n', 1, (0, 0, 139))
    screen.blit(string, (150, 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 130 <= x <= 430 and 190 <= y <= 240:  # переход к карте с уровнями
                    map()
                elif 130 <= x <= 430 and 270 <= y <= 320:  # переход к Обучению
                    pass
                elif 130 <= x <= 430 and 350 <= y <= 400:  # переход к настройкам
                    music()
                elif 130 <= x <= 430 and 430 <= y <= 510:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level_1()
                    level_2()
                    level_3()

                if event.key == pygame.K_2:
                    level_2()
                    level_3()

                if event.key == pygame.K_3:
                    level_3()

        pygame.display.flip()
        clock.tick(FPS)


def map():
    background = load_image('back2.jpg')
    star = load_image2('sky.PNG', -1)

    screen.blit(background, (0, 0))
    pygame.font.init()
    font = pygame.font.Font(None, 60)
    for i in range(3):
        screen.blit(star, (150 * i, 170 * i))
        koor = [(100, 70), (250, 240), (405, 410)]
        string = font.render(str(i + 1), 1, (255, 255, 255))
        screen.blit(string, koor[i])

    pygame.draw.polygon(screen, pygame.Color('RoyalBlue'),
                        ((20, 510), (60, 480), (170, 480), (170, 540), (60, 540)))
    string = pygame.font.Font(None, 40).render('Back', 1, pygame.Color('LightSkyBlue'))
    screen.blit(string, (70, 495))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 20 <= x <= 170 and 480 <= y <= 540:
                    start_screen()
                elif 0 <= x <= 220 and 20 <= y <= 135:
                    level_1()
                    level_2()
                elif 150 <= x <= 370 and 200 <= y <= 300:
                    level_2()
                    level_3()
                elif 300 <= x <= 525 and 350 <= y <= 490:
                    level_3()

        pygame.display.flip()
        clock.tick(FPS)


def final_screen():
    text = ['ИГРА ОКОНЧЕНА',
            '',
            'Количество пройденных уровней:',
            '']

    background = load_image('background.jpg')
    screen.blit(background, (0, 0))

    pygame.font.init()
    font = pygame.font.Font(None, 40)
    text_coord = 50

    for line in text:
        string = font.render(line, 1, pygame.Color('white'))
        string_rect = string.get_rect()
        text_coord = text_coord + 10
        string_rect.top = text_coord
        string_rect.x = 300
        text_coord = text_coord + string_rect.height
        screen.blit(string, string_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        pygame.display.flip()
        clock.tick(FPS)


def load_level(name):
    fullname = "data/" + name
    with open(fullname, 'r') as map_file:
        level_map = []
        for line in map_file:
            line = line.strip()
            level_map.append(line)
    return level_map


def generate_level(level_map):
    global trap
    new_player, x, y = None, None, None
    for y in range(len(level_map)):
        for x in range(len(level_map[y])):
            if level_map[y][x] == '.':
                Tile('wall.png', x, y)
            elif level_map[y][x] == '#':
                Tile('box.png', x, y)
            elif level_map[y][x] == '@':
                Tile('wall.png', x, y)
                new_player = Player(x, y)
            elif level_map[y][x] == '&':
                Tile('wall.png', x, y)
                fire = Fire(x, y)
            elif level_map[y][x] == '*':
                Tile('wall.png', x, y)
                trap = Trap(x, y)
    return new_player, x, y, fire, trap


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = load_image(tile_type)
        self.rect = self.image.get_rect().move(50 * pos_x, 50 * pos_y)

        self.add(tiles_group, all_sprites)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = load_image('magician.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(50 * pos_x, 50 * pos_y)
        self.pos = (pos_x, pos_y)
        self.add(player_group, all_sprites)

    def move_up(self):
        self.rect = self.rect.move(0, -50)

    def move_down(self):
        self.rect = self.rect.move(0, +50)

    def move_left(self):
        self.rect = self.rect.move(-50, 0)

    def move_right(self):
        self.rect = self.rect.move(+50, 0)


class Fire(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = load_image('fire.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(50 * pos_x, 50 * pos_y)

        self.add(fire_group, all_sprites)


class Trap(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = load_image('trap.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(50 * pos_x, 50 * pos_y)

        self.add(trap_group, all_sprites)


class Star(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = load_image2('star.jpg', -1)
        self.rect = self.image.get_rect()

        self.add(star_group)


start_screen()

terminate()
