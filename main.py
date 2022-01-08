from constans import *

back = pygame.image.load('data/bg.jpg')


# класс для мага
class Magician(pygame.sprite.Sprite):
    # Изначально маг смотрит вправо, поэтому right = True
    right = True

    def __init__(self):

        super().__init__()

        # Создание изображения для игрока(находится в папке data)

        self.image = pygame.image.load('data/idle.png')

        self.rect = self.image.get_rect()

        # Задаем вектор скорости игрока
        self.change_x = 0
        self.change_y = 0

    # функция для передвижения мага

    def update(self):
        #  устанавливаем для мага гравитацию
        self.count_gravitation()

        # Передвигаем мага  вправо/влево
        # change_x будет меняться позже при нажатии на стрелочки клавиатуры
        self.rect.x += self.change_x

        # проверка на столкновение с платформами
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        # Перебираем все возможные объекты, с которыми могли бы столкнуться
        for block in block_hit_list:
            # Если мы идем направо,
            # устанавливает нашу правую сторону на левой стороне предмета, которого мы ударили
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # В противном случае, если мы движемся влево, то делаем наоборот
                self.rect.left = block.rect.right

        # передвижение вверх/вниз
        self.rect.y += self.change_y

        # делаем то же самое, только для вверх вниз
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Устанавливаем нашу позицию на основе верхней / нижней части объекта, на который мы попали
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Останавливаем вертикальное движение
            self.change_y = 0

    # функция для вычисления гравитации при падении мага

    def count_gravitation(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .95

        # если маг на земле, то устаноим позицию Y = 0
        if self.rect.y >= screen_height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = screen_height - self.rect.height

    def jump(self):
        # Обработка прыжка
        #  нужно проверять здесь, контактируем ли мы с чем-либо
        # или другими словами, не находимся ли мы в полете.
        # Для этого опускаемся на 10 единиц, проверем соприкосновение и далее поднимаемся обратно
        self.rect.y += 10
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 10

        # Если все в порядке, прыгаем вверх
        if len(platform_hit_list) > 0 or self.rect.bottom >= screen_height:
            self.change_y = -16

    # Передвижение игрока
    def go_left(self):
        # Сами функции будут вызваны позже из основного цикла
        self.change_x = -9  # Двигаем игрока по Х
        if self.right:  # Проверяем куда он смотрит и если что, то переворачиваем его
            self.flip()
            self.right = False

    def go_right(self):
        # то же самое, но вправо
        self.change_x = 9
        if not self.right:
            self.flip()
            self.right = True

    def stop(self):
        # вызываем этот метод, когда не нажимаем на клавиши
        self.change_x = 0

    def flip(self):
        # переворот игрока (зеркальное отражение)
        self.image = pygame.transform.flip(self.image, True, False)


# Класс для  платформ
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):
        # Конструктор платформ
        super().__init__()

        self.image = pygame.image.load('data/platform.png')

        self.rect = self.image.get_rect()

# пока не готово
class Fire(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/fire.png')
        self.rect = self.image.get_rect()


# Класс для расстановки платформ на уровне
class Level(object):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.fire = pygame.sprite.Group()

        self.player = player

    # обновление чтобы рисовались платформы
    def update(self):
        self.platform_list.update()
        self.fire = pygame.sprite.Group()

    # функция для рисования объектов на уровне
    def draw(self, screen):
        # Рисуем задний фон
        screen.blit(back, (0, 0))

        # Рисуем все платформы из группы спрайтов
        self.platform_list.draw(screen)
        self.fire.draw(screen)


# Класс, что описывает где будут находится все платформы
# на определенном уровне игры
class Level_1(Level):
    def __init__(self, player):
        # Вызываем родительский конструктор
        Level.__init__(self, player)

        # Массив с данными про платформы. Данные в таком формате:
        # ширина, высота, x и y позиция
        level = [
            [210, 32, 500, 500],
            [210, 32, 200, 400],
            [210, 32, 600, 300],
        ]
        fires = [60, 60, 600, 500]

        # Перебираем массив и добавляем каждую платформу в группу спрайтов - platform_list
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)


# Основная функция программы
def main():
    pygame.init()

    size = [screen_width, screen_height]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Magician")

    # Создаем мага
    player = Magician()

    # Создаем все уровни
    level_list = []
    level_list.append(Level_1(player))

    # Устанавливаем текущий уровень
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = screen_height - player.rect.height
    active_sprite_list.add(player)

    running = False

    clock = pygame.time.Clock()

    while not running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        active_sprite_list.update()

        current_level.update()

        # Если игрок приблизится к правой стороне, то дальше его не двигаем
        if player.rect.right > screen_width:
            player.rect.right = screen_width

        # Если игрок приблизится к левой стороне, то дальше его не двигаем
        if player.rect.left < 0:
            player.rect.left = 0

        # Рисуем объекты на окне
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        clock.tick(FPS)

        pygame.display.flip()

    pygame.quit()
