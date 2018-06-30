from Overworld import *
from Player import *
from Monster import *
from Arena import *
from Screen import *


class Universe:
    """
        All of the Entities are stored here and are used in either Overworld or Arena depending on what stage is currently active
    """
    controls = ['w','a','s','d']

    def __init__(self, x, y):
        self.screen = Screen(x, y)
        self.x = x # Unused for now.
        self.y = y # Unused for now.
        self.isOverworld = True  # False if the current stage is the Arena
        self.overworld = Overworld(self, x, y)
        # Pulled Player ASCII art from http://www.ascii-art.de/ascii/s/stickman.txt.
        # (Darth Vader and Luke go at it!)
        self.player = Player(
            10, 2, ["@@@o@/", "@@/</@", "@/@\\@@", "/@@@\\@"], "P", 30, 10, 100)
        # array containing all monsters
        self.monsters = [
            Monster(-2, -2, ["\\@@A@@", "@\\/|>@", "@@@/\\@", "@@@\\@\\"], "M", 10, 10, 100)]
        self.arena = None  # we use startArena() to instantiate this
        self.loop()

    def startArena(self, monster):
        """
            Instantiates the arena against a monster and changes the stage
        :param monster:
        """
        self.isOverworld = False
        self.arena = Arena(self, self.player, monster, self.x, self.y)

    def loop(self):
        while(True):
            self.update(self.getInputs())
            self.draw(self.screen)


    def getInputs(self):
        return input(">>")

    def update(self, inputs):
        """
            updates either the Overworld or the Arena depending on which one is active
        :param inputs: most recent input
        """
        # This is for testing only.
        # TODO: Remove this once Overworld to Arena transition is implemented.
        self.isOverworld = False

        if self.isOverworld:
            self.overworld.update(inputs)
        else:
            if self.arena == None:
                # TODO: Pass in the appropriate monster here.
                self.startArena(self.monsters[0])
            self.arena.update(inputs)

    def draw(self, screen):
        """
            The screen is drawn using the Overworld or the Arena's draw() function
        :param screen:
        """
        if self.isOverworld:
            self.overworld.draw(screen)
        else:
            self.arena.draw(screen)
        screen.print()


game = Universe(30, 10)
