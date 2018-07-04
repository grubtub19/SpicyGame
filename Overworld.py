
from Player import *
from Monster import*

class Overworld:

    def __init__(self, universe, x, y):
        self.universe = universe
        self.x = x
        self.y = y

    def update(self, inputs):
        self.universe.player.update(inputs)
        for i in range(len(self.universe.monsters)):
            if (self.universe.player.x == self.universe.monsters[i].x):
                # and self.universe.player.y == self.universe.monsters[i].y):
                print("Y")
                self.universe.startArena(i)
            
    def draw(self, screen):
        self.universe.player.drawOverworld(screen)
        self.universe.monsters[0].drawOverworld(screen)
