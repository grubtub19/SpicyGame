from ArenaHealthBars import *
from time import sleep
import random
import sys

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

    def doPlayerAttack(self):
        """Draws and prints intermediate frames for the player's attack animation."""
        # Player raises sword.
        self.arenaHealthBars.draw(self.universe.screen)
        self.player.sprite = self.player.startAttackSprite
        # This needs to be 2 because there's an extra line in this ASCII art.
        self.player.moveInArena(5, 2)
        self.player.drawArena(self.universe.screen)
        self.monster.moveInArena(19, 3)
        self.monster.drawArena(self.universe.screen)
        self.universe.screen.print()
        sleep(2)

        self.player.calcAttack(self.player.moveset[0], self.monster)
        # Player swings sword.
        self.arenaHealthBars.draw(self.universe.screen)
        self.player.sprite = self.player.endAttackSprite
        self.player.moveInArena(14, 3)
        self.player.drawArena(self.universe.screen)
        # Monster flinches.
        self.monster.sprite = self.monster.flinchSprite
        self.monster.drawArena(self.universe.screen)
        self.universe.screen.print()
        sleep(2)

        # Update player and monster ASCII with the original positions
        # for the start of the usual draw step.
        self.player.applyAttack(self.player.moveset[0], self.monster)
        self.arenaHealthBars.draw(self.universe.screen)
        self.player.moveInArena(5, 3)
        self.player.sprite = self.player.neutralSprite
        self.monster.moveInArena(19, 3)
        self.player.drawArena(self.universe.screen)
        self.monster.sprite = self.monster.neutralSprite
        self.monster.drawArena(self.universe.screen)
        self.universe.screen.print()
        sleep(2)

    def doMonsterAttack(self):
        """Draws and prints intermediate frames for the monster's attack animation."""
        # Monster raises sword.

        self.arenaHealthBars.draw(self.universe.screen)

        self.monster.sprite = self.monster.startAttackSprite
        self.monster.drawArena(self.universe.screen)

        self.player.moveInArena(5, 3)
        self.player.drawArena(self.universe.screen)

        self.universe.screen.print()
        sleep(2)

        # Monster swings sword.
        self.monster.calcAttack(self.monster.moveset[0], self.player)
        self.arenaHealthBars.draw(self.universe.screen)

        self.player.sprite = self.player.flinchSprite
        self.player.drawArena(self.universe.screen)

        # Player flinches.
        self.monster.sprite = self.monster.endAttackSprite
        self.monster.moveInArena(9, 3)
        self.monster.drawArena(self.universe.screen)

        self.universe.screen.print()
        sleep(2)

        # Update player and monster ASCII with the original positions
        # for the start of the usual draw step.
        self.monster.applyAttack(self.monster.moveset[0], self.player)
        self.monster.moveInArena(19, 3)
        self.monster.sprite = self.monster.neutralSprite
        self.player.moveInArena(5, 3)
        self.player.sprite = self.player.neutralSprite

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

            # TODO: We'll need to remember the last position of Player in
            # the Overworld so we can revert to it in case we run.

            # Destroy Arena and return to Overworld.
            self.universe.arena = None
            self.universe.isOverworld = True

        if inputs == 'a':
            # TODO: Either remove this or turn it into a useful dialog.
            print('attack')

            # TODO: The health bar update after the player's hit lands
            # is less than optimal. Fix this. Test it out to see
            # what I mean, I'm short on time right now.

            # Hacky drawing of intermediate action frames here.
            self.doPlayerAttack()

            # Damage is applied after the intermediate action frames show
            # the attack successfully landing. This results in the
            # health bar being shown to shorten only after the attack lands.
            # Otherwise, the health bar is shown to shorten before the
            # attack even lands.
            # TODO: Allow for variable attack input.

        if self.monster.currentHealth > 0:
            #same as above but with the monster
            self.doMonsterAttack()
        else:
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

        if self.player.currentHealth <= 0:
            # Player defeated.
            # TODO: Draw and print defeat screen.
            print('DEFEAT')

            # TODO: Provide the option to start a new game here?
            sleep(5)

            # Remove player
            del self.universe.player

            # This clean up needs to happen after the drawn screen is
            # drawn and printed, otherwise there won't be an Arena to refer
            # to.
            self.universe.arena = None
            self.universe.isOverworld = True

            # Terminate game.
            sys.exit()

    def draw(self, screen):
        self.player.drawArena(screen)
        self.monster.drawArena(screen)
        self.arenaHealthBars.draw(screen)
