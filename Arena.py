from ArenaHealthBars import *


class Arena:
    def __init__(self, player, monster, x, y):
        self.player = player
        self.monster = monster
        self.healthBars = ArenaHealthBars(player, monster)
        self.x = x  # screen dimensions just in case we need them
        self.y = y
        self.state = 0 # Not sure how the actual arena code will work, but if there are different phases or turns, using states might come in handy

    def update(self, inputs):
        """
            Good luck coding this
        :param inputs:

        """
        pass

    def draw(self, screen):
        self.player.drawArena(screen)
        self.monster.drawArena(screen)
        self.healthBars.draw(screen)