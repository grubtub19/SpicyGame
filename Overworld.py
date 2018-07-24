from Player import *
from Monster import*
from HealthPot import *
from Helper import *
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

        # Load Overworld legend sprites.
        self.overworldCharactersLegend = Entity(
            overworld_x=108, overworld_y=8,
            sprite=[],
            overworldChar=Helper.loadSprite(
                'sprites/overworldCharactersLegend.txt'),
            arena_x=0, arena_y=0)

        self.overworldControlsLegend = Entity(
            overworld_x=40, overworld_y=8,
            sprite=[],
            overworldChar=Helper.loadSprite(
                'sprites/overworldControlsLegend.txt'),
            arena_x=0, arena_y=0)

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
                self.universe.textBox.print("+600 Health")
                self.universe.textBox.print("Use the health potion? (y/n)")
                self.draw(self.universe.screen)
                self.universe.textBox.wipeScreen()
                self.universe.screen.print()
                foo = input()

                while not(foo == "y" or foo == "n"):
                    self.universe.textBox.print("Invalid Input")
                    self.universe.textBox.print("+600 Health")
                    self.universe.textBox.print("Use the health potion? (y/n)")
                    self.draw(self.universe.screen)
                    self.universe.textBox.wipeScreen()
                    self.universe.screen.print()
                    foo = input()

                if foo == "y":
                    self.universe.player.currentHealth = self.universe.player.currentHealth + self.universe.healthpot[i].health

                    if self.universe.player.currentHealth > self.universe.player.maxHealth:
                        self.universe.player.currentHealth = self.universe.player.maxHealth

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

        # Draw Overworld characters legend.
        self.overworldCharactersLegend.drawOverworld(screen)

        # Draw Overworld controls legend.
        self.overworldControlsLegend.drawOverworld(screen)

        # Draw Player health bar.
        self.universe.playerHealthBar.drawOverworld(screen)

        # Draws monsters.
        for i in range(len(self.universe.monsters)):
            self.universe.monsters[i].drawOverworld(screen)

        #Draws health pot
        for i in range(len(self.universe.healthpot)):
            self.universe.healthpot[i].drawOverworld(screen)

        if self.universe.textBox.hasContent():
            self.universe.textBox.drawBox(self.universe.screen)

        # Draw player.
        self.universe.player.drawOverworld(screen)
