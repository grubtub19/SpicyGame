from ArenaHealthBars import *
from time import sleep
import random

class Arena:
    def __init__(self, universe, player, monsterIndex, x, y):
        self.universe = universe # Easy access to universe.
        self.player = player
        self.player.arena_x = 5 # Initial player position in Arena.
        self.player.arena_y = 3
        self.monsterIndex = monsterIndex
        self.monster = self.universe.monsters[monsterIndex]
        self.monster.arena_x = 19 # Initial monster position in Arena.
        self.monster.arena_y = 3
        self.arenaHealthBars = ArenaHealthBars(player, self.monster)
        self.x = x  # screen dimensions just in case we need them
        self.y = y
        self.state = 0 # Not sure how the actual arena code will work, but if there are different phases or turns, using states might come in handy

    def animatePlayerAttack(self):
        """Draws and prints intermediate frames for the player's attack animation."""

        # Player raises sword.
        self.player.ASCII = ["_____@", "@@\o/@",
                                "@@/@@@", "@/@\@@", "/@@@\\@"]
        # This needs to be 2 because there's an extra line in this ASCII art.
        self.player.move(5, 2)
        self.player.drawArena(self.universe.screen)
        self.monster.move(19, 3)
        self.monster.drawArena(self.universe.screen)
        self.universe.screen.print()
        print()
        sleep(0.5)

        # Player swings sword.
        self.player.ASCII = ["@@@o@@", "@@/\@@", "@/@\\\@", "/@@@\\\\"]
        self.player.move(14, 3)
        self.player.drawArena(self.universe.screen)
        # Monster flinches.
        self.monster.ASCII = ["@@\A/@", "@@@|@|", "@@/\@|", "@@\@\\|"]
        self.monster.drawArena(self.universe.screen)
        self.universe.screen.print()
        print()
        sleep(0.5)

        # Update player and monster ASCII with the original positions
        # for the start of the usual draw step.
        self.player.move(5, 3)
        self.player.ASCII = ["@@@o@/", "@@/</@", "@/@\@@", "/@@@\@"]
        self.monster.move(19, 3)
        self.monster.ASCII = ["\@@A@@", "@\/|>@", "@@@/\@", "@@@\@\\"]

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
            # TODO: Either remove this or turn it into a useful dialog.
            print('attack')

            self.player.attack(self.monster)

            # Hacky drawing of intermediate action frames here.
            self.animatePlayerAttack()

        if self.monster.currentHealth <= 0:
            # Any number <10 will cause 0 bars to be drawn for the health bar.
            # So although the monster technically still has health left,
            # it's misleading and bad UX to draw 0 bars.

            # Monster defeated.
            # TODO: Draw and print victory screen.
            print('VICTORY!')

            # Remove monster from monster list.
            del self.universe.monsters[self.monsterIndex]

            # This clean up needs to happen after the victory screen is
            # drawn and printed, otherwise there won't be an Arena to refer
            # to.
            self.universe.arena = None
            self.universe.isOverworld = True

        # TODO: Implement monster attack.


    def draw(self, screen):
        self.player.drawArena(screen)
        self.monster.drawArena(screen)
        self.arenaHealthBars.draw(screen)
