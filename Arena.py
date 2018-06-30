from ArenaHealthBars import *
from time import sleep

class Arena:
    def __init__(self, universe, player, monster, x, y):
        self.universe = universe # Easy access to universe.
        self.player = player
        self.monster = monster
        self.arenaHealthBars = ArenaHealthBars(player, monster)
        self.x = x  # screen dimensions just in case we need them
        self.y = y
        self.state = 0 # Not sure how the actual arena code will work, but if there are different phases or turns, using states might come in handy

    def update(self, inputs):
        """
        :param inputs: User input.
        """
        acceptable_inputs = ['a', 'r']

        if len(inputs) != 1 or inputs not in acceptable_inputs:
            print('Invalid input')
            return

        if inputs == 'r':
            # Run away.
            print('run away')

            # Destroy Arena and return to Overworld.
            self.universe.arena = None
            self.universe.isOverworld = True

        if inputs == 'a':
            print('attack')
            # Attack.

            # TODO: Factor in defense power into calculation.

            # Apply player attack to monster.
            self.monster.currentHealth -= self.player.attackPower

            # Hacky drawing of intermediate action frames here.
            # Player raises sword.
            self.player.ASCII = ["_____@", "@@\o/@", "@@/@@@", "@/@\@@", "/@@@\\@"]
            self.player.drawArena(self.universe.screen, 5, 2)
            self.monster.drawArena(self.universe.screen, 19, 3)
            self.universe.screen.print()
            print()
            sleep(0.5)

            # Player swings sword.
            self.player.ASCII = ["@@@o@@", "@@/\@@", "@/@\\\@", "/@@@\\\\"]
            self.player.drawArena(self.universe.screen, 14, 3)
            # Monster flinches.
            self.monster.ASCII = ["@@\A/@", "@@@|@|", "@@/\@|", "@@\@\\|"]
            self.monster.drawArena(self.universe.screen, 19, 3)
            self.universe.screen.print()
            print()
            sleep(0.5)

            # Update player and monster ASCII with the original positions
            # for the start of the usual draw step.
            self.player.ASCII = ["@@@o@/", "@@/</@", "@/@\@@", "/@@@\@"]
            self.monster.ASCII = ["\@@A@@", "@\/|>@", "@@@/\@", "@@@\@\\"]

        if self.monster.currentHealth <= 0:
            # Monster defeated.
            # TODO: Draw and print victory screen.
            self.universe.arena = None
            self.universe.isOverworld = True


    def draw(self, screen):
        # Hard code these since we don't mind them being in the same spot each time.
        self.player.drawArena(screen, 5, 3)
        self.monster.drawArena(screen, 19, 3)
        self.arenaHealthBars.draw(screen)
