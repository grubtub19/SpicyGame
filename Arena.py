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

        # Just an example of how to access the textBox
        # TODO: Use the textBox instead of printing to the console
        self.universe.textBox.print("Normal Attack -> a")
        self.universe.textBox.print("Run Away      -> r")

        # For scaling the animation speed.
        self.animationSpeedScale = 1

    def doPlayerAttack(self):
        """
            Draws and prints intermediate frames for the player's attack animation.
        """

        ########## Frame 1 ###########
        #   -> Player Raises sword
        #   -> Monster is Neutral
        #   -> 0.5 time scale

        # Draw health bars.
        self.universe.playerHealthBar.drawArena(self.universe.screen)
        self.universe.currentMonsterHealthBar.drawArena(self.universe.screen)

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


        ########## Frame 2 ###########
        #   -> Player Moves to Attack Location
        #   -> Player Swipes Sword
        #   -> Monster Flinches
        #   -> Damage is calculated and saved in Monster (applies next frame)
        #   -> Damage Numbers Appear
        #   -> 1.0 time scale

        # Draw health bars.
        self.universe.playerHealthBar.drawArena(self.universe.screen)
        self.universe.currentMonsterHealthBar.drawArena(self.universe.screen)

        # Calculate attack and saves values in Monster (applies next frame)
        self.player.calcAttack(self.player.moveset[0], self.monster)

        # Monster flinches.
        self.monster.sprite = self.monster.flinchSprite
        self.monster.drawArena(self.universe.screen)

        # Player commences attack.
        self.player.sprite = self.player.endAttackSprite
        self.player.moveInArena(self.playerAttackX, self.playerY)
        self.player.drawArena(self.universe.screen)

        # Monster's damage is taken on this frame, so draw the damage numbers
        self.monster.damageText.drawArena(self.universe.screen)

        # Print frame and sleep for 1.0 time scale
        self.universe.screen.print()
        sleep(1/self.animationSpeedScale)


        ########## Frame 3 ###########
        #   -> Both Player and Monster in neutral
        #   -> Damage is applied to monster and health bar moves
        #   -> 0.5 time scale

        # Apply attack and draw changed health bars
        self.player.applyAttack(self.player.moveset[0], self.monster)
        self.universe.playerHealthBar.drawArena(self.universe.screen)
        self.universe.currentMonsterHealthBar.drawArena(self.universe.screen)

        # Reset Player to neutral position and neutral sprite
        self.player.sprite = self.player.neutralSprite
        self.player.moveInArena(self.playerNeutralX, self.playerY)
        self.player.drawArena(self.universe.screen)

        # Reset Monster to neutral position and neutral sprite
        self.monster.sprite = self.monster.neutralSprite
        self.monster.moveInArena(self.monsterNeutralX, self.monsterY)
        self.monster.drawArena(self.universe.screen)

        # Print frame and sleep for 0.5 time scale
        self.universe.screen.print()
        sleep(1/self.animationSpeedScale * 0.5)


        ########## Frame 3.5 ###########
        #   -> This frame only occurs if the monster has status effects
        #   -> Monster Flinches
        #   -> Status damage is applied to monster
        #   -> Monster's damage text is drawn
        #   -> 1.0 time scale
        self.doMonsterStatusEffects()

    def doMonsterAttack(self):
        """
            Draws and prints intermediate frames for the monster's attack animation.
        """

        ########## Frame 1 ###########
        #   -> Monster prepares attack
        #   -> Player is Neutral
        #   -> 0.5 time scale

        # Print health bars.
        self.universe.playerHealthBar.drawArena(self.universe.screen)
        self.universe.currentMonsterHealthBar.drawArena(self.universe.screen)

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


        ########## Frame 2 ###########
        #   -> Monster Moves to Attack Location
        #   -> Monster attacks player
        #   -> Player flinches (we don't have a flinching art tho)
        #   -> Damage is calculated and saved in player (applied next frame)
        #   -> Player's Damage Numbers Appear
        #   -> 1.0 time scale

        # Draw health bars.
        self.universe.playerHealthBar.drawArena(self.universe.screen)
        self.universe.currentMonsterHealthBar.drawArena(self.universe.screen)

        # Calculate attack to be applied during the next frame.
        self.monster.calcAttack(self.monster.moveset[0], self.player)

        # Player flinches.
        self.player.sprite = self.player.flinchSprite
        self.player.moveInArena(self.playerNeutralX, self.playerY)
        self.player.drawArena(self.universe.screen)

        # Monster attacks
        self.monster.sprite = self.monster.endAttackSprite
        self.monster.moveInArena(self.monsterAttackX, self.monsterY)
        self.monster.drawArena(self.universe.screen)

        # Player's damage is taken on this frame, so draw the damage numbers
        self.player.damageText.drawArena(self.universe.screen)

        # Print frame.
        self.universe.screen.print()
        sleep(1 / self.animationSpeedScale)


        ########## Frame 3 ###########
        #   -> Both Player and Monster in neutral
        #   -> Damage is applied to player and health bar moves
        #   -> 0.5 time scale

        # Apply attack to player and draws changed health bar
        self.monster.applyAttack(self.monster.moveset[0], self.player)
        self.universe.playerHealthBar.drawArena(self.universe.screen)
        self.universe.currentMonsterHealthBar.drawArena(self.universe.screen)

        # Reset Monster to neutral position and neutral sprite
        self.monster.sprite = self.monster.neutralSprite
        self.monster.moveInArena(self.monsterNeutralX, self.monsterY)
        self.monster.drawArena(self.universe.screen)

        # Reset Player to neutral position and neutral sprite
        self.player.sprite = self.player.neutralSprite
        self.player.moveInArena(self.playerNeutralX, self.playerY)
        self.player.drawArena(self.universe.screen)

        # Print frame at 0.5 time scale
        self.universe.screen.print()
        sleep(1 / self.animationSpeedScale * 0.5)


        ########## Frame 3.5 ###########
        #   -> This frame only occurs if the player has status effects
        #   -> Player Flinches
        #   -> Status damage is applied to player
        #   -> Player's damage text is drawn
        #   -> 1.0 time scale
        self.doPlayerStatusEffects()

    def doMonsterStatusEffects(self):
        #   -> This frame only occurs if the monster has status effects
        #   -> Monster Flinches
        #   -> Status damage is applied to monster
        #   -> Monster's damage text is drawn
        #   -> 1.0 time scale

        if self.monster.applyStatusEffects():
            self.player.drawArena(self.universe.screen)
            self.monster.sprite = self.monster.flinchSprite
            self.monster.drawArena(self.universe.screen)
            self.universe.playerHealthBar.drawArena(self.universe.screen)
            self.universe.currentMonsterHealthBar.drawArena(
                self.universe.screen)
            self.monster.damageText.drawArena(self.universe.screen)
            self.universe.screen.print()
            sleep(1 / self.animationSpeedScale)

    def doPlayerStatusEffects(self):
        #   -> This frame only occurs if the player has status effects
        #   -> Player Flinches
        #   -> Status damage is applied to player
        #   -> Player's damage text is drawn
        #   -> 1.0 time scale

        if self.player.applyStatusEffects():
            print("next is ui update")
            self.player.drawArena(self.universe.screen)
            self.monster.drawArena(self.universe.screen)
            self.universe.playerHealthBar.drawArena(self.universe.screen)
            self.universe.currentMonsterHealthBar.drawArena(
                self.universe.screen)
            self.player.damageText.drawArena(self.universe.screen)
            self.universe.screen.print()
            sleep(1 / self.animationSpeedScale)

        #   -> Extra frame is printed so that player's statusEffect damageText does not remain on screen while inputting
            self.player.drawArena(self.universe.screen)
            self.monster.drawArena(self.universe.screen)
            self.universe.playerHealthBar.drawArena(self.universe.screen)
            self.universe.currentMonsterHealthBar.drawArena(
                self.universe.screen)
            self.player.statusUI.draw(self.universe.screen)
            self.universe.screen.print()

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
            # TODO: Draw and print a small victory screen?
            print('VICTORY!')
            sleep(2)

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
        self.universe.playerHealthBar.drawArena(self.universe.screen)
        self.universe.currentMonsterHealthBar.drawArena(self.universe.screen)
