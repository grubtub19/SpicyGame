class Entity:

    transparent = "T" # This character is ignored when drawing the ASCII art

    def __init__(self, x, y, ASCII, overworldChar):
        self.x = x
        self.y = y
        # defines the origin at the top left of the ASCII art. Example of 3x3 ASCII art below. "O" is the position of the x, y values
        #      O X X
        #      X X X
        #      X X X
        self.ASCII = ASCII  #Arena - Array of Strings (2D)
        self.overworldChar = overworldChar # single char

    def draw(self, screen, ASCII):
        """
            "Draws" the Entity's ASCII on the screen starting from x, y and drawing to the right and down
        :param screen:
        :param ASCII: either arena or overworld ASCII
        """
        for i in range(0, len(ASCII)):
            for j in range(0, len(ASCII[i])):
                if ASCII[i][j] != Entity.transparent: # ignore any transparent values currently "T"
                    try:
                        screen[self.y + i][self.x + j] = ASCII[i][j]
                    except IndexError:
                        print("out of bounds")

    def drawArena(self, screen):
        """
            draws the Arena ASCII
        :param screen:
        """
        self.draw(screen, self.ASCII)

    def drawOverworld(self, screen):
        """
            Draws the Overworld ASCII
        :param screen:
        """
        self.draw(screen, self.overworldChar)


