from Player import *
from Monster import*
from HealthPot import *
import sys

class Overworld:

    def __init__(self, universe, width, height, overworld_x, overworld_y):
        self.universe = universe

        # Dimensions of the Overworld space on the Overworld screen.
        self.width = width
        self.height = height

        # Coordinates of the Overworld space on the Overworld screen.
        self.overworld_x = overworld_x
        self.overworld_y = overworld_y

    def update(self, inputs):
        if inputs == 'q':
            res = input('Are you sure you want to quit? (y/n) >> ')
            if res == 'y' or 'q':
                sys.exit()

        # Update player position.
        self.universe.player.update(inputs, self)

        for i in range(len(self.universe.monsters)):
            # Check if player is in same position as monster.
            if (self.universe.player.overworld_x == self.universe.monsters[i].overworld_x and self.universe.player.overworld_y == self.universe.monsters[i].overworld_y):
                # Start battle.
                self.universe.startArena(i)
                
        for i in range(len(self.universe.healthpot)):
            # Check if player is in same position as health pot.
            if (self.universe.player.overworld_x == self.universe.healthpot[i].overworld_x and self.universe.player.overworld_y == self.universe.healthpot[i].overworld_y):
                
                #ask if player wants health pot or not
                foo = input("Do you want to use this health pot? (y/n)")
                                    
                while not(foo == "y" or foo == "n"):
                    print ("Not a valid input")
                    foo = input("Do you want to use this health pot? (y/n)")
                        
                if foo == "y":
                    self.universe.player.currentHealth = self.universe.player.currentHealth + self.universe.healthpot[i].health
                    del self.universe.healthpot[i]
                    print ("You have used the health pot!")
                    break
                    
                if foo == "n":
                    print ("ok")
                    
                    
                

    def draw(self, screen):
        # Draw the Overworld border.
        for i in range(self.overworld_y, self.overworld_y + self.height + 1):
            for j in range(self.overworld_x, self.overworld_x + self.width + 1):
                if j == self.overworld_x or j == self.overworld_x + self.width:
                    screen.buffer[i][j] = '|'
                if i == self.overworld_y or i == self.overworld_y + self.height:
                    screen.buffer[i][j] = '-'

        # Draw player.
        self.universe.player.drawOverworld(screen)

        # Draws monsters.
        for i in range(len(self.universe.monsters)):
            self.universe.monsters[i].drawOverworld(screen)
            
        #Draws health pot
        for i in range(len(self.universe.healthpot)):
            self.universe.healthpot[i].drawOverworld(screen)
