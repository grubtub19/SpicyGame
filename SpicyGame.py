from Universe import *


class SpicyGame:
    x = 30      # size of "display"
    y = 10
    blankChar = "."
    def __init__(self):
        self.universe = Universe(SpicyGame.x, SpicyGame.y)      # initialize game world
        self.screen = [[SpicyGame.blankChar for i in range(0, SpicyGame.x)] for j in range(0, SpicyGame.y)] # this is the ASCII "display" with a x, y coordinate system starting at the top left

        self.draw() # since loop() starts with input(), we draw() so the game doesn't start blank
        self.loop()

    def loop(self):
        """
            3 Steps: get player input -> update everything -> print out everything to the console
        """
        while(True):
            self.update(self.getInputs())
            self.draw()

    def getInputs(self):
        return input(">>")

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

    def wipeScreen(self):
        """
        resets the screen to be blank (made up of "blankChar"s)
        """
        self.screen = [[SpicyGame.blankChar for i in range(0, SpicyGame.x)] for j in range(0, SpicyGame.y)]

    def print(self):
        """
        print the screen to the console. If you want the screen updated without waiting for user input, you need to call something like wait(100) and SpicyGame.print()
        :return:
        """
        for line in self.screen:
            for char in line:
                print(char + "  ", end='')
            print()

game = SpicyGame()