from Entity import *


class Pokemon(Entity):
    """
        Any Entity that can battle is a Pokemon (Player, Monster)
    """
    def __init__(self, x, y, ASCII, overworldChar, attackPower, defensePower, health):
        Entity.__init__(self, x, y, ASCII, overworldChar)
        self.attackPower = attackPower
        self.defensePower = defensePower
        self.maxHealth = health
        self.currentHealth = health