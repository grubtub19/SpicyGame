from Pokemon import *


class Player(Pokemon):

    controls = ['w', 'a', 's', 'd'] # [up, left, down, right]

    def __init__(self, overworld_x, overworld_y, sprites_path, overworldChar, arena_x, arena_y,
    defensePower, health, evade,  crit, moveset):
        Pokemon.__init__(self, overworld_x, overworld_y, sprites_path,
                         overworldChar, arena_x, arena_y, defensePower, health, evade, crit, moveset)

    def update(self, inputs, overworld):
        """Used in the Overworld, moves the character in the
        cardinal directions based on input, without letting the character
        leave the Overworld borders.

        :param inputs:
        :param overworld: Used to check the Overworld's borders.
        :return:
        """
        if inputs == self.controls[0]:
            # W.
            if self.overworld_y - 1 > overworld.overworld_y:
                self.overworld_y = self.overworld_y - 1
        elif inputs == self.controls[1]:
            # A.
            if self.overworld_x - 1 > overworld.overworld_x:
                self.overworld_x = self.overworld_x - 1
        elif inputs == self.controls[2]:
            # S.
            if self.overworld_y + 1 < overworld.overworld_y + overworld.height:
                self.overworld_y = self.overworld_y + 1
        elif inputs == self.controls[3]:
            # D.
            if self.overworld_x + 1 < overworld.overworld_x + overworld.width:
                self.overworld_x = self.overworld_x + 1
