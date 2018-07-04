from Pokemon import *


class Monster(Pokemon):
    def __init__(self, x, y, ASCII, overworldChar, attackPower, defensePower, health, crit):
        Pokemon.__init__(self, x, y, ASCII, overworldChar, attackPower, defensePower, health, crit)

