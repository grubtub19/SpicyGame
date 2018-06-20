from Player import *
from Monster import *
from Overworld import *
from Arena import *

class Universe:
    """
        All of the Entities are stored here and are used in either Overworld or Arena depending on what stage is currently active
    """
    controls = ['w','a','s','d']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isOverworld = True  # False if the current stage is the Arena
        self.overworld = Overworld(self, x, y)
        self.player = Player(10, 2, ["TT___TT","T/   \T","|     |","T\   /T", "TT---TT"], "P", 10, 10, 100) # note that "T" is transparent
        self.monsters = [Monster(-2, -2, ["MONSTER","MADNESS"], "M", 10, 10, 100)]  # array containing all monsters
        self.arena = None  # we use startArena to instantiate this

    def startArena(self, monster):
        """
            Instantiates the arena against a monster and changes the stage
        :param monster:
        """
        self.isOverworld = False
        self.arena = Arena(self.player, monster, self.x, self.y)

    def update(self, inputs):
        """
            updates either the Overworld or the Arena depending on which one is active
        :param inputs: most recent input
        """
        self.startArena(self.monsters[0])
        if self.isOverworld:
            self.overworld.update(inputs)
        else:
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


