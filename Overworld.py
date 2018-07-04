
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
            
            #checks if player is in same position as monster
            if (self.universe.player.overworld_x == self.universe.monsters[i].overworld_x and self.universe.player.overworld_y == self.universe.monsters[i].overworld_y):

                #start battle
                self.universe.startArena(i)
            
    def draw(self, screen):
        self.universe.player.drawOverworld(screen)
        self.universe.monsters[0].drawOverworld(screen)
