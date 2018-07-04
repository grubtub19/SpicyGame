class Screen:

    blankChar = "."

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.buffer = [[self.blankChar for i in range(0, self.x)] for j in range(0, self.y)]

    def wipeScreen(self):
        """
        resets the screen to be blank (made up of "blankChar"s)
        """
        self.buffer = [[self.blankChar for i in range(0, self.x)] for j in range(0, self.y)]

    def print(self):
        """Prints the buffer's contents to the console."""
        # This is an initial attemp to print some whitespace above the drawn
        # frames so that past frames don't show up in the console.
        # This way, we'll have a better illusion of real animation.
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        for line in self.buffer:
            for char in line:
                # Not having spaces results in prettier ASCII art.
                print(char, end='')
            print()
        self.wipeScreen()
