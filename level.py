from Lvl import levels
from main import *


class Level:
    def __init__(self, current_level, surface, create_overworld):

        # Настройки
        self.display_surface = surface  # экран
        self.current_level = current_level  # Выбранный уровень
        level_data = levels[current_level]  # Инфа об уровне (Подробней в Lvl.py)
        level_content = level_data['content']  # Надпись
        self.new_max_level = level_data['unlock']  # Следующий уровень
        self.create_overworld = create_overworld  # функция класса Game (cм Шаблон), вызывает карту

        # Просто фраза
        self.font = pygame.font.Font(None, 40)
        self.text_surf = self.font.render(level_content, True, 'White')
        self.text_rect = self.text_surf.get_rect(center=(screen_width / 2, screen_height / 2))

    # осуществляет выход из уровня
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:  # Enter - здесь будет условие прохождения уровня
            self.create_overworld(self.current_level, self.new_max_level)
        if keys[pygame.K_ESCAPE]:  # Выйти из уровня можно, нажав Esc (лево-верх)
            self.create_overworld(self.current_level, 0)

    def run(self):
        self.input()
        # здесь должен вызываться уровень
        self.display_surface.blit(self.text_surf, self.text_rect)
        if self.current_level == 0:
            main()
