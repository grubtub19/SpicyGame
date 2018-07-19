class HealthPot:

    def __init__(self, overworld_x, overworld_y, overworldChar, ASCII, health):

        self.overworld_x = overworld_x
        self.overworld_y = overworld_y
        self.overworldChar = overworldChar
        self.ASCII = ASCII
        self.health = health

    def draw(self, screen, ASCII, x, y):
        """Draws the health pot's ASCII art on the screen starting from x, y,
        then moving rightwards and then downwards.
        """
        for i in range(0, len(ASCII)):
            for j in range(0, len(ASCII[i])):
                # if ASCII[i][j] != HealthPot.transparent: # ignore any transparent values.
                try:
                    screen.buffer[y + i][x + j] = ASCII[i][j]
                except IndexError:
                    print("out of bounds")

    def drawOverworld(self, screen):
        self.draw(screen, self.overworldChar, self.overworld_x,self.overworld_y)
