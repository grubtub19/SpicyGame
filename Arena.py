from ArenaHealthBars import *
from time import sleep
import random
import sys

class Arena:

    def __init__(self, universe, player, monsterIndex):
        # Easy access to universe.
        self.universe = universe

        # Initialize Player.
        self.player = player
        self.playerNeutralX = 40
        self.playerAttackX = 76
        self.playerY = 3
        self.player.arena_x = self.playerNeutralX
        self.player.arena_y = self.playerY

        # Initialize Monster.
        self.monsterIndex = monsterIndex
        self.monster = self.universe.monsters[monsterIndex]
        self.monsterNeutralX = 85
        self.monsterAttackX = 47
        self.monsterY = 5
        self.monster.arena_x = self.monsterNeutralX
        self.monster.arena_y = self.monsterY

        # Initialize ArenaHealthBars.
        self.arenaHealthBars = ArenaHealthBars(player, self.monster)

        # For scaling the animation speed.
        self.animationSpeedScale = 1

    def doPlayerAttack(self):
        """Draws and prints intermediate frames for the player's attack animation."""
        # Frame 1.
        # Draw health bars.
        self.arenaHealthBars.draw(self.universe.screen)

        # Player starts attack.
        self.player.sprite = self.player.startAttackSprite
        self.player.moveInArena(self.playerNeutralX, self.playerY - 2)
        self.player.drawArena(self.universe.screen)

        # Monster stays neutral.
        self.monster.moveInArena(self.monsterNeutralX, self.monsterY)
        self.monster.drawArena(self.universe.screen)

        # Print frame.
        self.universe.screen.print()
        sleep(1/self.animationSpeedScale * 0.5)

        # Frame 2.
        # Draw health bars.
        self.arenaHealthBars.draw(self.universe.screen)

        # Monster flinches.
        self.monster.sprite = self.monster.flinchSprite
        self.monster.drawArena(self.universe.screen)

        # Player ends attack.
        # Calculate attack to be applied during the next frame.
        self.player.calcAttack(self.player.moveset[0], self.monster)
        self.player.sprite = self.player.endAttackSprite
        self.player.moveInArena(self.playerAttackX, self.playerY)
        self.player.drawArena(self.universe.screen)

        # Print frame.
        self.universe.screen.print()
        sleep(1/self.animationSpeedScale)

        # Frame 3.
        # Apply attack so that health bars are drawn according
        # to the Monster's updated health. Then draw health bars.
        self.player.applyAttack(self.player.moveset[0], self.monster)
        self.arenaHealthBars.draw(self.universe.screen)

        # Update Player with the original positions
        # and sprites for the start of the usual draw step.
        self.player.sprite = self.player.neutralSprite
        self.player.moveInArena(self.playerNeutralX, self.playerY)
        self.player.drawArena(self.universe.screen)

        # Update Monster with the original positions
        # and sprites for the start of the usual draw step.
        self.monster.sprite = self.monster.neutralSprite
        self.monster.moveInArena(self.monsterNeutralX, self.monsterY)
        self.monster.drawArena(self.universe.screen)

        # Print frame.
        self.universe.screen.print()
        sleep(1/self.animationSpeedScale)

    def doMonsterAttack(self):
        """Draws and prints intermediate frames for the monster's attack animation."""
        # Frame 1.
        # Print health bars.
        self.arenaHealthBars.draw(self.universe.screen)

        # Monster starts attack.
        self.monster.sprite = self.monster.startAttackSprite
        self.monster.moveInArena(self.monsterNeutralX, self.monsterY)
        self.monster.drawArena(self.universe.screen)

        # Player stays neutral.
        self.player.moveInArena(self.playerNeutralX, self.playerY)
        self.player.drawArena(self.universe.screen)

        # Print frame.
        self.universe.screen.print()
        sleep(1/self.animationSpeedScale * 0.5)

        # Frame 2.
        # Draw health bars.
        self.arenaHealthBars.draw(self.universe.screen)

        # Player flinches.
        self.player.sprite = self.player.flinchSprite
        self.player.moveInArena(self.playerNeutralX, self.playerY)
        self.player.drawArena(self.universe.screen)

        # Monster ends attack.
        # Monster is drawn after Player so that Monster's attack sprite
        # is visible over the Player.
        # Calculate attack to be applied during the next frame.
        self.monster.calcAttack(self.monster.moveset[0], self.player)
        self.monster.sprite = self.monster.endAttackSprite
        self.monster.moveInArena(self.monsterAttackX, self.monsterY)
        self.monster.drawArena(self.universe.screen)

        # Just an example of how to access the textBox
        self.universe.textBox.print("Normal Attack -> 'a'")
        self.universe.textBox.print("Strong Attack -> 's'")
        self.universe.textBox.print("Weak Attack -> 'd'")

        # Print frame.
        self.universe.screen.print()
        sleep(1 / self.animationSpeedScale)

        # Frame 3.
        # Apply attack so that health bars are drawn according
        # to the Player's updated health. Then draw health bars.
        self.monster.applyAttack(self.monster.moveset[0], self.player)
        self.arenaHealthBars.draw(self.universe.screen)

        # Update Monster with the original positions
        # and sprites for the start of the usual draw step.
        self.monster.sprite = self.monster.neutralSprite
        self.monster.moveInArena(self.monsterNeutralX, self.monsterY)
        self.monster.drawArena(self.universe.screen)

        # Update Player with the original positions
        # and sprites for the start of the usual draw step.
        self.player.sprite = self.player.neutralSprite
        self.player.moveInArena(self.playerNeutralX, self.playerY)
        self.player.drawArena(self.universe.screen)

        # Print frame.
        self.universe.screen.print()

    def doMonsterStatusEffects(self):
        if self.monster.applyStatusEffects():
            pass
            #TODO: Update monster Status Effects UI

    def doPlayerStatusEffects(self):
        if self.player.applyStatusEffects():
            pass
            #TODO: Update player Status Effects UI

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

            return

        if inputs == 'a':
            # TODO: Either remove this or turn it into a useful dialog.
            print('attack')

            # TODO: The health bar update after the player's hit lands
            # is less than optimal. Fix this. Test it out to see
            # what I mean, I'm short on time right now.

            # Hacky drawing of intermediate action frames here.
            self.doPlayerAttack()
            self.doMonsterStatusEffects()

            # Damage is applied after the intermediate action frames show
            # the attack successfully landing. This results in the
            # health bar being shown to shorten only after the attack lands.
            # Otherwise, the health bar is shown to shorten before the
            # attack even lands.
            # TODO: Allow for variable attack input.

        if self.monster.currentHealth > 0:
            #same as above but with the monster
            self.doMonsterAttack()
            self.doPlayerStatusEffects()
        else:
            # Monster defeated.
            # TODO: Draw and print victory screen.
            print('VICTORY!')

            # Remove monster from monster list.
            del self.universe.monsters[self.monsterIndex]
            self.player.currStatusEffects = []
            # This clean up needs to happen after the victory screen is
            # drawn and printed, otherwise there won't be an Arena to refer
            # to.
            self.universe.arena = None
            self.universe.isOverworld = True

        if self.player.currentHealth <= 0:
            # Player defeated.
            f = open("sprites/defeatScreen.txt", "r")
            defeatScreen = f.read()
            print(defeatScreen)

            sleep(1)

            #option to restart the game
            isValid = False
            self.universe.exit = True
            while not isValid:
                replay = input("continue? (y or n): ")
                if replay == "y":
                    self.universe.reset = True
                    isValid = True
                elif replay == "n":
                    isValid = True


                else:
                    print("invalid input try again!")




    def draw(self, screen):
        self.player.drawArena(screen)
        self.monster.drawArena(screen)
        self.arenaHealthBars.draw(screen)
