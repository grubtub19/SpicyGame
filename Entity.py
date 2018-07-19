class Entity:

    transparent = "@" # This character is ignored when drawing the ASCII art

    def __init__(self, overworld_x, overworld_y, sprite, overworldChar, arena_x, arena_y):
        # Entity's coordinates.
        self.overworld_x = overworld_x
        self.overworld_y = overworld_y
        self.arena_x = arena_x
        self.arena_y = arena_y

        # The origin/start of an Entity's ASCII art is the top left corner.
        # Example of 3x3 ASCII art below. "O" is defined by x, y in the
        # Overworld/Arena.
        #      O X X
        #      X X X
        #      X X X
        self.sprite = sprite  # In the Arena, the ASCII art is a 2D matrix of strings.
        self.overworldChar = overworldChar # Character that represents the entity in the Overworld.

    def setSprite(self, sprite_path):
        """Assumes that there is no trailing newline at the end
        end of the .txt file."""
        with open(sprite_path) as f:
            sprite = []
            for line in f:
                sprite.append(line.rstrip())
        self.sprite = sprite

    def draw(self, screen, ASCII, x, y):
        """Draws the Entity's ASCII art on the screen starting from x, y,
        then moving rightwards and then downwards.

        :param screen:
        :param ASCII: Either arena or overworld ASCII
        """
        for i in range(0, len(ASCII)):
            for j in range(0, len(ASCII[i])):
                if ASCII[i][j] != Entity.transparent: # ignore any transparent values.
                    try:
                        screen.buffer[y + i][x + j] = ASCII[i][j]
                    except IndexError:
                        print("out of bounds")

    def moveInArena(self, x, y):
        """Moves the entity to the specified x, y coordinates in the Arena.

        This should only be used in Arena."""
        self.arena_x = x
        self.arena_y = y

    def drawArena(self, screen):
        """Draws a sprite in the Arena.

        :param screen:
        """
        self.draw(screen, self.sprite, self.arena_x, self.arena_y)

    def drawOverworld(self, screen):
        """Draws a character in the Overworld.

        :param screen:
        """
        self.draw(screen, self.overworldChar, self.overworld_x,self.overworld_y)
