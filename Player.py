from Pokemon import *


class Player(Pokemon):

    controls = ['w', 'a', 's', 'd'] # [up, left, down, right]

    def __init__(self, x, y, ASCII, overworldChar, attackPower, defensePower, health):
        Pokemon.__init__(self, x, y, ASCII, overworldChar, attackPower, defensePower, health)

    def update(self, inputs):
        """
            Used in the Overworld, moves the character in the cardinal directions based on input
        :param inputs:
        :return:
        """
        if inputs == self.controls[0]:
            print("changing y from " + str(self.y) + " to " + str(self.y - 1))
            self.y = self.y - 1
        elif inputs == self.controls[1]:
            self.x = self.x - 1
        elif inputs == self.controls[2]:
            self.y = self.y + 1
        elif inputs == self.controls[3]:
            self.x = self.x + 1