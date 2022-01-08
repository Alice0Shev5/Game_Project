from map_level import *

# здесь соберем все окна
# 1 - меню, 2 - карта, 3 - помощь-инструкция, 4-8 - уровни


def start_screen():  # меню игры - стартовое окно
    pygame.init()
    pygame.display.set_caption("Magician")
    screen.blit(background, (0, 0))
    #
    pygame.font.init()
    font = pygame.font.Font(None, 40)
    # Надписи и эллипсы
    text = {'Карта': [200, 190, 300, 200], 'Помощь': [200, 270, 290, 280],
            'Настройки': [200, 350, 280, 360], 'Выход': [200, 430, 300, 440]}
    for key, zn in text.items():
        if key == 'Выход':
            pygame.draw.ellipse(screen, pygame.Color('sienna'), (200, 430, 300, 50))
        else:
            pygame.draw.ellipse(screen, (233, 233, 200), (zn[0], zn[1], 300, 50))
        string = font.render(key, 1, pygame.Color('burlywood'))
        screen.blit(string, (zn[2], zn[3]))
    string = pygame.font.Font(None, 60).render('M a g i c a i n', 1, pygame.Color('steelblue'))
    screen.blit(string, (220, 80))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # если нажата кнопка мыши, проверяем возможные ответы
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 200 <= x <= 500 and 190 <= y <= 240:  # переход к карте с уровнями
                    map()
                elif 200 <= x <= 500 and 270 <= y <= 320:  # переход к Обучению
                    pass
                elif 200 <= x <= 500 and 350 <= y <= 400:  # переход к настройкам
                    pass
                elif 200 <= x <= 500 and 430 <= y <= 510:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(FPS)


def map():  # окно с картой
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 640 <= x <= 790 and 520 <= y <= 570:
                    start_screen()
        screen.blit(background, (0, 0))
        game.run()
        pygame.display.update()
        clock.tick(60)


start_screen()
