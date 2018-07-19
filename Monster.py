from Pokemon import *


class Monster(Pokemon):
    def __init__(self, overworld_x, overworld_y, sprites_path, overworldChar, arena_x, arena_y, defensePower, health, evade, crit, moveset):
        Pokemon.__init__(self, overworld_x, overworld_y, sprites_path,
                         overworldChar, arena_x, arena_y, defensePower, health, evade, crit, moveset)
