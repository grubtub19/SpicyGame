class Screen:

    blankChar = "."

    def __init__(self, universe, width, height):
        self.universe = universe
        self.width = width
        self.height = height
        self.buffer = [[self.blankChar for i in range(0, self.width)] for j in range(0, self.height)]

    def wipeScreen(self):
        """
        resets the screen to be blank (made up of "blankChar"s)
        """
        self.buffer = [[self.blankChar for i in range(0, self.width)] for j in range(0, self.height)]

    def print(self):
        # TODO: optionally draw the textBox since we don't want it on some screens like the start menu
        self.universe.textBox.drawBox(self.universe.screen)
        """Prints the buffer's contents to the console."""
        # This is an initial attempt to print some whitespace above the drawn
        # frames so that past frames don't show up in the console.
        # This way, we'll have a better illusion of real animation.
        # TODO: Do some math to accommodate having dialog printed near the
        # frame, alongside the whitespace lines. Otherwise it's just oblivion.
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        for line in self.buffer:
            for char in line:
                # Not having spaces results in prettier ASCII art.
                print(char, end='')
            print()
        self.wipeScreen()
