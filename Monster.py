from Pokemon import *


class Monster(Pokemon):
    def __init__(self, overworld_x, overworld_y, ASCII, overworldChar, attackPower, defensePower, health, crit):
        Pokemon.__init__(self, overworld_x, overworld_y, ASCII, overworldChar, attackPower, defensePower, health, 0, 0, crit)
