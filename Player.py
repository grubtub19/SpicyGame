from Pokemon import *


class Player(Pokemon):

    controls = ['w', 'a', 's', 'd'] # [up, left, down, right]

    def __init__(self, overworld_x, overworld_y, ASCII, overworldChar, arena_x, arena_y,
    defensePower, health, crit, moveset):
        Pokemon.__init__(self, overworld_x, overworld_y, ASCII,
                         overworldChar, arena_x, arena_y, defensePower, health, crit, moveset)

    def update(self, inputs):
        """
            Used in the Overworld, moves the character in the cardinal directions based on input
        :param inputs:
        :return:
        """
        if inputs == self.controls[0]:
            print("changing y from " + str(self.overworld_y) + " to " + str(self.overworld_y - 1))
            self.overworld_y = self.overworld_y - 1
        elif inputs == self.controls[1]:
            self.overworld_x = self.overworld_x - 1
        elif inputs == self.controls[2]:
            self.overworld_y = self.overworld_y + 1
        elif inputs == self.controls[3]:
            self.overworld_x = self.overworld_x + 1
