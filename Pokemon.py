from Entity import *


class Pokemon(Entity):
    """
        Any Entity that can battle is a Pokemon (Player, Monster)
    """
    def __init__(self, overworld_x, overworld_y, ASCII, overworldChar, attackPower, defensePower, health, arena_x, arena_y):
        Entity.__init__(self, overworld_x, overworld_y, ASCII, overworldChar, arena_x, arena_y)
        self.attackPower = attackPower
        self.defensePower = defensePower
        self.maxHealth = health
        self.currentHealth = health