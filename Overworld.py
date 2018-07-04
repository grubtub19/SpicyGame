from Player import *
from Monster import*
import sys

class Overworld:

    def __init__(self, universe, x, y):
        self.universe = universe
        self.x = x # Screen dimensions.
        self.y = y

    def update(self, inputs):
        # TODO: Evaluate if this might be more appropriate in Universe.
        if inputs == 'q':
            res = input('Are you sure you want to quit? (y/n) >> ')
            if res == 'y' or 'q':
                sys.exit()

        # Update player position.
        self.universe.player.update(inputs)

        for i in range(len(self.universe.monsters)):
            # Check if player is in same position as monster.
            if (self.universe.player.overworld_x == self.universe.monsters[i].overworld_x and self.universe.player.overworld_y == self.universe.monsters[i].overworld_y):
                # Start battle.
                self.universe.startArena(i)

    def draw(self, screen):
        # Draw player.
        self.universe.player.drawOverworld(screen)

        # Draw monsters.
        for i in range(len(self.universe.monsters)):
            self.universe.monsters[i].drawOverworld(screen)
