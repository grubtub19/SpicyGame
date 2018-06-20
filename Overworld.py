from Universe import *


class Overworld:
    def __init__(self, universe, x, y):
        self.universe = universe
        self.x = x
        self.y = y

    def update(self, inputs):
        self.universe.player.update(inputs)

    def draw(self, screen):
        self.universe.player.drawOverworld(screen)
