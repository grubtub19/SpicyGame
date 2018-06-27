from Universe import *


class SpicyGame:

    def __init__(self):
        self.universe = Universe(SpicyGame.x, SpicyGame.y)      # initialize game world
         # this is the ASCII "display" with a x, y coordinate system starting at the top left

        self.draw() # since loop() starts with input(), we draw() so the game doesn't start blank
        self.loop()




    def update(self, inputs):
        """
            This function is "passed down" from broad classes to more specific classes

            SpicyGame
            |
             -> Universe
                |
                 -> Overworld or Arena
                    |
                     -> Entities

            """
        self.universe.update(inputs)

    def draw(self):
        """
        passed down the same as update()
        -------
        Parameters
        screem      Need a pointer to the screen so that other draw() functions can modify it
        """
        self.universe.draw(self.screen)
        self.print()
        self.wipeScreen()



