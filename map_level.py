from map_draw import Overworld
from level import Level
from constans import *


# осуществляет переход от карты к уровню
class Game:
    def __init__(self):
        self.max_level = 1
        self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        self.status = 'overworld'  # в зависимости от статуса идет
        #                            переход или к карте, или к уровню

    def create_level(self, current_level):
        self.level = Level(current_level, screen, self.create_overworld)
        self.status = 'level'

    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()


game = Game()
