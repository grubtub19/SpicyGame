from Pokemon import *


class Monster(Pokemon):
    def __init__(self, overworld_x, overworld_y, ASCII, sprites, overworldChar, arena_x, arena_y, defensePower, health, crit, moveset):
        Pokemon.__init__(self, overworld_x, overworld_y, ASCII, sprites,
                         overworldChar, arena_x, arena_y, defensePower, health, crit, moveset)
