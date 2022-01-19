# в этом файле находятся классы с описанием всех спрайтов(персонажей и тайлов)
from constans import *


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

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(50 * self.pos[0], 50 * self.pos[1])

    # def move_up(self):
    # self.rect = self.rect.move(0, -50)

    # def move_down(self):
    # self.rect = self.rect.move(0, +50)

    # def move_left(self):
    # self.rect = self.rect.move(-50, 0)

    # def move_right(self):
    # self.rect = self.rect.move(+50, 0)


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