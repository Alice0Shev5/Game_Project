import pygame
import sys

size = width, height = (550, 550)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 60

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
fire_group = pygame.sprite.Group()


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
    player, level_x, level_y, fire = generate_level(load_level("level_1.txt"))

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

            if not pygame.sprite.collide_rect(player, fire):
                screen.fill(pygame.Color(0, 0, 0))
                tiles_group.draw(screen)
                player_group.draw(screen)
                fire_group.draw(screen)
            else:
                all_sprites.empty()
                player_group.empty()
                tiles_group.empty()
                fire_group.empty()
                return

        pygame.display.flip()
        clock.tick(FPS)



def level_2():
    player, level_x, level_y, fire = generate_level(load_level("level_2.txt"))

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

        if not pygame.sprite.collide_rect(player, fire):
            screen.fill(pygame.Color(0, 0, 0))
            tiles_group.draw(screen)
            player_group.draw(screen)
            fire_group.draw(screen)
        else:
            all_sprites.empty()
            player_group.empty()
            tiles_group.empty()
            fire_group.empty()
            final_screen()

        pygame.display.flip()
        clock.tick(FPS)


def start_screen():

    text = ["ЗАСТАВКА",
            "",
            "Правила игры",
            "Для выбора уровня - ",
            "нажмите 1 или 2"]



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
        string_rect.x = 200
        text_coord = text_coord + string_rect.height
        screen.blit(string, string_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level_1()
                    level_2()

                if event.key == pygame.K_2:
                    level_2()

        pygame.display.flip()
        clock.tick(FPS)


def final_screen():
    text = ["ЗАСТАВКА",
            "",
            "КОНЕЦ",
            " ",
            ""]



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
            # цветок будет обозначен на карте уровня знаком "&"
            elif level_map[y][x] == '&':
                Tile('wall.png', x, y)
                fire = Fire(x, y)
    return new_player, x, y, fire


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


start_screen()


terminate()
