class Entity:

    transparent = "@" # This character is ignored when drawing the ASCII art

    def __init__(self, overworld_x, overworld_y, ASCII, overworldChar, arena_x, arena_y):
        
        #overworld x and y
        self.overworld_x = overworld_x
        self.overworld_y = overworld_y
        
        #positions for arena/ batt;e
        self.arena_x = arena_x
        self.arena_y = arena_y
        # defines the origin at the top left of the ASCII art. Example of 3x3 ASCII art below. "O" is the position of the x, y values
        #      O X X
        #      X X X
        #      X X X
        self.ASCII = ASCII  #Arena - Array of Strings (2D)
        self.overworldChar = overworldChar # single char

    def draw(self, screen, ASCII, x, y):
        """
            "Draws" the Entity's ASCII on the screen starting from x, y and drawing to the right and down
        :param screen:
        :param ASCII: either arena or overworld ASCII
        """
        for i in range(0, len(ASCII)):
            for j in range(0, len(ASCII[i])):
                if ASCII[i][j] != Entity.transparent: # ignore any transparent values.
                    try:
                        screen.buffer[y + i][x + j] = ASCII[i][j]
                    except IndexError:
                        print("out of bounds")

    def move(self, x, y):
        """Moves the entity to the specified x, y coordinates"""
        self.x = x
        self.y = y

    def drawArena(self, screen):
        """
            draws the Arena ASCII
        :param screen:
        """
        self.draw(screen, self.ASCII, self.arena_x, self.arena_y)

    def drawOverworld(self, screen):
        """
            Draws the Overworld ASCII
        :param screen:
        """
        self.draw(screen, self.overworldChar, self.overworld_x,self.overworld_y)
