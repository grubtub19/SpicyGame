from time import sleep
import random
import sys
from Stats import *

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

        self.controls = Entity(0,0,["@------------------------@@@-------------------------@@@------------------------@@@---------------",
                                    "|   Heavy Attack   'a'   |@|   Normal Attack   's'   |@|   Light Attack   'd'   |@|   Run   'r'   |",
                                    "@------------------------@@@-------------------------@@@------------------------@@@---------------"],"", 35, 17)
        # For scaling the animation speed.
        self.animationSpeedScale = 1

    def drawEverything(self, healthBar, textBox, controls, player, monster, playerDamage, monsterDamage):
        if healthBar:
            self.universe.playerHealthBar.drawArena(self.universe.screen)
            self.universe.currentMonsterHealthBar.drawArena(self.universe.screen)
        if textBox:
            if self.universe.textBox.hasContent():
                self.universe.textBox.drawBox(self.universe.screen)
        if controls:
            self.controls.drawArena(self.universe.screen)
        if player:
            self.player.drawArena(self.universe.screen)
        if monster:
            self.monster.drawArena(self.universe.screen)
        if playerDamage:
            self.player.damageText.drawArena(self.universe.screen)
        if monsterDamage:
            self.monster.damageText.drawArena(self.universe.screen)

    def doPlayerAttack(self, inputs):
        """
            Draws and prints intermediate frames for the player's attack animation.
        """
        # different moveset
        if inputs == "a":
            moveNum = 0
        elif inputs == "s":
            moveNum = 1
        elif inputs == "d":
            moveNum = 2
        ########## Frame 1 ###########
        #   -> Player Raises sword
        #   -> Monster is Neutral
        #   -> 0.5 time scale

        # Player starts attack.
        self.player.sprite = self.player.startAttackSprite
        self.player.moveInArena(self.playerNeutralX, self.playerY - 2)

        # Monster stays neutral.
        self.monster.moveInArena(self.monsterNeutralX, self.monsterY)

        self.drawEverything(healthBar=True, textBox=True, controls=True, player=True, monster=True, playerDamage=False, monsterDamage=False)
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

        # Calculate attack and saves values in Monster (applies next frame)
        #Saves attack damage in counter for stats

        damageInfStat = self.player.calcAttack(self.player.moveset[moveNum], self.monster)
        self.universe.damageInflicted += damageInfStat

        # Monster flinches.
        self.monster.sprite = self.monster.flinchSprite

        # Player commences attack.
        self.player.sprite = self.player.endAttackSprite
        self.player.moveInArena(self.playerAttackX, self.playerY)

        self.drawEverything(healthBar=True, textBox=True, controls=True, player=True, monster=True, playerDamage=False, monsterDamage=True)

        # Print frame and sleep for 1.0 time scale
        self.universe.screen.print()
        sleep(1/self.animationSpeedScale)


        ########## Frame 3 ###########
        #   -> Both Player and Monster in neutral
        #   -> Damage is applied to monster and health bar moves
        #   -> 0.5 time scale

        # Apply attack and draw changed health bars
        self.player.applyAttack(self.player.moveset[moveNum], self.monster)

        # Reset Player to neutral position and neutral sprite
        self.player.sprite = self.player.neutralSprite
        self.player.moveInArena(self.playerNeutralX, self.playerY)

        # Reset Monster to neutral position and neutral sprite
        self.monster.sprite = self.monster.neutralSprite
        self.monster.moveInArena(self.monsterNeutralX, self.monsterY)

        self.drawEverything(healthBar=True, textBox=True, controls=True, player=True, monster=True, playerDamage=False, monsterDamage=False)

        # Print frame and sleep for 0.5 time scale
        self.universe.screen.print()
        sleep(1/self.animationSpeedScale * 0.5)


        ########## Frame 3.5 ###########
        #   -> This frame only occurs if the monster has status effects
        #   -> Monster Flinches
        #   -> Status damage is applied to monster
        #   -> Monster's damage text is drawn
        #   -> 1.0 time scale

        monster_healthPreEffect = self.monster.currentHealth

        self.doMonsterStatusEffects()

        monster_healthPostEffect = self.monster.currentHealth

        self.universe.damageInflicted = self.universe.damageInflicted + (monster_healthPreEffect - monster_healthPostEffect)

    def doMonsterAttack(self):
        """
            Draws and prints intermediate frames for the monster's attack animation.
        """
        #random monster attacks option
        #amoveNum = random.choices([0, 1, 2], [0.08, 0.46, 0.46])[0]
        weighted_choices = [(0, 8), (1, 46), (2, 46)]
        moveNum = random.choice([val for val, cnt in weighted_choices for i in range(cnt)])


        ########## Frame 1 ###########
        #   -> Monster prepares attack
        #   -> Player is Neutral
        #   -> 0.5 time scale

        # Monster starts attack.
        self.monster.sprite = self.monster.startAttackSprite
        self.monster.moveInArena(self.monsterNeutralX, self.monsterY)

        # Player stays neutral.
        self.player.moveInArena(self.playerNeutralX, self.playerY)

        self.drawEverything(healthBar=True, textBox=True, controls=True, player=True, monster=True, playerDamage=False, monsterDamage=False)

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

        # Calculate attack to be applied during the next frame.
        damageRecStat = self.monster.calcAttack(self.monster.moveset[moveNum], self.player)
        self.universe.damageReceived += damageRecStat

        # Player flinches.
        self.player.sprite = self.player.flinchSprite
        self.player.moveInArena(self.playerNeutralX, self.playerY)

        # Monster attacks
        self.monster.sprite = self.monster.endAttackSprite
        self.monster.moveInArena(self.monsterAttackX, self.monsterY)

        self.drawEverything(healthBar=True, textBox=True, controls=True, player=True, monster=True, playerDamage=True, monsterDamage=False)

        # Print frame.
        self.universe.screen.print()
        sleep(1 / self.animationSpeedScale)


        ########## Frame 3 ###########
        #   -> Both Player and Monster in neutral
        #   -> Damage is applied to player and health bar moves
        #   -> 0.5 time scale

        # Apply attack to player and draws changed health bar
        self.monster.applyAttack(self.monster.moveset[moveNum], self.player)

        # Reset Monster to neutral position and neutral sprite
        self.monster.sprite = self.monster.neutralSprite
        self.monster.moveInArena(self.monsterNeutralX, self.monsterY)

        # Reset Player to neutral position and neutral sprite
        self.player.sprite = self.player.neutralSprite
        self.player.moveInArena(self.playerNeutralX, self.playerY)

        self.drawEverything(healthBar=True, textBox=True, controls=True, player=True, monster=True, playerDamage=False, monsterDamage=False)

        # Print frame at 0.5 time scale
        self.universe.screen.print()
        sleep(1 / self.animationSpeedScale * 0.5)


        ########## Frame 3.5 ###########
        #   -> This frame only occurs if the player has status effects
        #   -> Player Flinches
        #   -> Status damage is applied to player
        #   -> Player's damage text is drawn
        #   -> 1.0 time scale

        player_healthPreEffect = self.player.currentHealth

        self.doPlayerStatusEffects()

        player_healthPostEffect = self.player.currentHealth

        #adds damage from effect to damageReceived in Universe for stats
        self.universe.damageReceived = self.universe.damageReceived + ( player_healthPreEffect - player_healthPostEffect)

    def doMonsterStatusEffects(self):
        #   -> This frame only occurs if the monster has status effects
        #   -> Monster Flinches
        #   -> Status damage is applied to monster
        #   -> Monster's damage text is drawn
        #   -> 1.0 time scale

        if self.monster.applyStatusEffects():
            self.monster.sprite = self.monster.flinchSprite
            self.drawEverything(healthBar=True, textBox=True, controls=True, player=True, monster=True,
                                playerDamage=False, monsterDamage=False)
            self.universe.screen.print()
            sleep(1 / self.animationSpeedScale)

    def doPlayerStatusEffects(self):
        #   -> This frame only occurs if the player has status effects
        #   -> Player Flinches
        #   -> Status damage is applied to player
        #   -> Player's damage text is drawn
        #   -> 1.0 time scale

        if self.player.applyStatusEffects():
            self.drawEverything(healthBar=True, textBox=True, controls=True, player=True, monster=True,
                                playerDamage=False, monsterDamage=False)
            self.universe.screen.print()
            sleep(1 / self.animationSpeedScale)

        #   -> Extra frame is printed so that player's statusEffect damageText does not remain on screen while inputting
            self.drawEverything(healthBar=True, textBox=True, controls=True, player=True, monster=True,
                                playerDamage=False, monsterDamage=False)
            self.universe.screen.print()

    def update(self, inputs):
        """
        :param inputs: User input.
        """
        acceptable_inputs = ['a','s','d','r']

        if len(inputs) != 1 or inputs not in acceptable_inputs:
            self.universe.textBox.print("Invalid Input")
            self.universe.textBox.drawBox(self.universe.screen)
            self.drawEverything(True, True, True, True, True, False, False)
            self.universe.screen.print()
            self.universe.textBox.wipeScreen()
            return

        if inputs == 'r':
            # Destroy Arena and return to Overworld.
            self.universe.arena = None
            self.universe.isOverworld = True

            return

        else:
            self.doPlayerAttack(inputs)
        if self.monster.currentHealth > 0:
            #same as above but with the monster
            self.doMonsterAttack()
        else:
            # Monster defeated.
            self.universe.textBox.print("VICTORY!")
            self.drawEverything(True, True, True, True, True, False, False)
            self.universe.screen.print()
            self.universe.textBox.wipeScreen()
            sleep(2)

            # Remove monster from monster list.
            del self.universe.monsters[self.monsterIndex]
            self.player.currStatusEffects = []
            self.player.statusUI.visibleEffects = []
            # This clean up needs to happen after the victory screen is
            # drawn and printed, otherwise there won't be an Arena to refer
            # to.
            self.universe.arena = None
            self.universe.isOverworld = True

        if self.player.currentHealth <= 0:

            #Calculates Final score
            self.universe.score = self.universe.damageInflicted - self.universe.damageReceived

            # Player defeated.
            self.universe.textBox.print("Score: " + str(self.universe.score))
            self.universe.textBox.print("Please write your name: ")
            defeat = Entity(0,0,"","",60,0)
            defeat.setSprite("sprites/defeatScreen.txt")
            defeat.drawArena(self.universe.screen)
            self.drawEverything(healthBar=False, textBox=True, controls=False, player=False, monster=False,
                                playerDamage=False, monsterDamage=False)
            self.universe.textBox.wipeScreen()
            self.universe.screen.print()

            #print score in a new file

            name = input()
            Stats.WriteFile(name, self.universe)
            self.universe.textBox.print("Game stats exported")
            self.universe.textBox.print("to %s.txt" % name)

            #option to restart the game
            isValid = False
            self.universe.exit = True

            while not isValid:
                # Player defeated.
                self.universe.textBox.print("Continue? (y/n)")
                defeat.drawArena(self.universe.screen)
                self.drawEverything(healthBar=False, textBox=True, controls=False, player=False, monster=False,
                                    playerDamage=False, monsterDamage=False)
                self.universe.textBox.wipeScreen()
                self.universe.screen.print()

                replay = input()
                if replay == "y":
                    self.universe.reset = True
                    isValid = True
                elif replay == "n":
                    isValid = True
                else:
                    self.universe.textBox.print("Invalid Input")

        #Checks if any monsters left (i.e. if game is won)

        if (len(self.universe.monsters)==0):

            self.universe.score = self.universe.damageInflicted - self.universe.damageReceived

            self.universe.textBox.print("Score: " + str(self.universe.score))
            self.universe.textBox.print("Please write your name: ")
            winner = Entity(0, 0, "", "", 60, 0)
            winner.setSprite("sprites/winnerScreen.txt")
            winner.drawArena(self.universe.screen)
            self.drawEverything(healthBar=False, textBox=True, controls=False, player=False, monster=False,
                                playerDamage=False, monsterDamage=False)
            self.universe.textBox.wipeScreen()
            self.universe.screen.print()

            name = input()
            Stats.WriteFile(name, self.universe)
            self.universe.textBox.print("Game stats exported")
            self.universe.textBox.print("to %s.txt" % name)

            #option to restart the game
            isValid = False
            self.universe.exit = True
            while not isValid:
                self.universe.textBox.print("Play Again? (y/n)")
                winner.drawArena(self.universe.screen)
                self.drawEverything(healthBar=False, textBox=True, controls=False, player=False, monster=False,
                                    playerDamage=False, monsterDamage=False)
                self.universe.textBox.wipeScreen()
                self.universe.screen.print()

                replay = input()
                if replay == "y":
                    self.universe.reset = True
                    isValid = True
                elif replay == "n":
                    isValid = True
                else:
                    self.universe.textBox.print("Invalid Input")



    def draw(self, screen):
        self.drawEverything(healthBar=True, textBox=True, controls=True, player=True, monster=True, playerDamage=False, monsterDamage=False)
