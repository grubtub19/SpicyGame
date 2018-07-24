from Overworld import *
from Player import *
from Monster import *
from Arena import *
from Screen import *
from Attack import *
from StatusEffect import *
from HealthBar import *
from TextBox import *
from HealthPot import *


class Universe:
    """
        All of the Entities are stored here and are used in either Overworld or Arena depending on what stage is currently active
    """
    controls = ['w','a','s','d']

    def __init__(self, screen_width, screen_height):

        self.screen = Screen(self, screen_width, screen_height)
        self.screen_width = screen_width
        self.screen_height = screen_height

        start = Entity(0,0,"","",45,0)
        start.setSprite("sprites/startingScreen.txt",)
        start.drawArena(self.screen)
        self.screen.print()
        self.textBox = TextBox(0,15)

        self.isOverworld = True  # False if the current stage is the Arena
        self.overworld = Overworld(
            self, width=40, height=11, overworld_x=60, overworld_y=4)

        self.player = Player(
            overworld_x=81, overworld_y=9,
            sprites_path="sprites/player.txt",
            overworldChar="P", arena_x=50, arena_y=10, defensePower=100, evade=0.2,

            health=1000, crit=0.2, moveset=[
                Attack(name='Heavy Attack', damage=450, hitChance=0.3, statusEffect=StatusEffect(name="Shock", duration=6, damagePerTurn=40, sprite_path="sprites/shockEffect.txt")),
                Attack(name='Regular Attack', damage=150, hitChance=0.7, statusEffect=StatusEffect(name="Poison", duration=4, damagePerTurn=20, sprite_path="sprites/poisonEffect.txt")),
                Attack(name='Light Attack', damage=60, hitChance=1, statusEffect=StatusEffect(name="Spice", duration=6, damagePerTurn=40, sprite_path="sprites/spiceEffect.txt"))
            ])
        # array containing all monsters
        self.monsters = [
            Monster(
                overworld_x=84, overworld_y=11,
                sprites_path='sprites/pepperSprite.txt',
                overworldChar="M", arena_x=30, arena_y=10, defensePower=20, health=1000, evade=0.1, crit=0.3,
                moveset=[
                    Attack(name='Ultimate attack', damage=300, hitChance=0.9999,
                           statusEffect=StatusEffect(name="Poison", duration=4, damagePerTurn=37, sprite_path="sprites/poisonEffect.txt")),
                    Attack(name='Spice Attack', damage=160, hitChance=0.7,
                           statusEffect=StatusEffect(name="Shock", duration=6, damagePerTurn=8, sprite_path="sprites/shockEffect.txt")),
                    Attack(name='Light Attack', damage=120, hitChance=1,
                           statusEffect=StatusEffect(name="Spice", duration=3, damagePerTurn=14, sprite_path="sprites/spiceEffect.txt"))
                ]),
            #devil pepper ascci
            Monster(
                overworld_x=74, overworld_y=8,
                sprites_path='sprites/pepperSprite.txt',
                overworldChar="M", arena_x=30, arena_y=10, defensePower=10, health=600, evade=0.1, crit=0.6,
                moveset=[
                    Attack(name='Ultimate attack', damage=250, hitChance=0.9999,
                           statusEffect=StatusEffect(name="Spice", duration=6, damagePerTurn=38, sprite_path="sprites/spiceEffect.txt")),
                    Attack(name='Regular Attack', damage=240, hitChance=0.6),
                    Attack(name='Light Attack', damage=200, hitChance=1,
                           statusEffect=StatusEffect(name="Spice", duration=3, damagePerTurn=6, sprite_path="sprites/spiceEffect.txt"))
                ]),
            #fire pepper assci orsomething
            Monster(
                overworld_x=88, overworld_y=8,
                sprites_path='sprites/pepperSprite.txt',
                overworldChar="M", arena_x=30, arena_y=10, defensePower=50, health=1500, evade=0.1, crit=0.3,
                moveset=[
                    Attack(name='Ultimate attack', damage=100, hitChance=0.9999,
                           statusEffect=StatusEffect(name="Spice", duration=4, damagePerTurn=78, sprite_path="sprites/spiceEffect.txt")),
                    Attack(name='Regular Attack', damage=50, hitChance=0.7,
                           statusEffect=StatusEffect(name="Shock", duration=4, damagePerTurn=70, sprite_path="sprites/shockEffect.txt")),
                    Attack(name='Light Attack', damage=30, hitChance=1,
                           statusEffect=StatusEffect(name="Poison", duration=5, damagePerTurn=68, sprite_path="sprites/poisonEffect.txt"))
                ])
        ]

        self.playerHealthBar = HealthBar(self.player)

        self.healthpot = [
            HealthPot(overworld_x=78, overworld_y=11, overworldChar = "+", ASCII = ["+"], health = 400),
            HealthPot(overworld_x=84, overworld_y=7, overworldChar = "+", ASCII = ["+"], health = 400)
        ]

        #Counters for stats
        self.damageInflicted = 0
        self.damageReceived = 0
        self.score = 0

        self.arena = None
        self.reset = False
        self.exit = False
        self.loop()

    def startArena(self, monsterIndex):
        """
            Instantiates the arena against a monster and changes the stage
        :param monster:
        """
        self.isOverworld = False
        self.arena = Arena(self, self.player, monsterIndex)
        self.currentMonsterHealthBar = HealthBar(self.monsters[monsterIndex])
        self.arena.draw(self.screen)
        self.screen.print()

    def loop(self):
        while not self.exit:
            self.update(self.getInputs())

            if not self.exit and self.isOverworld:
                self.drawOverworld()

    def getInputs(self):
        return input('>> ')

    def update(self, inputs):
        """
            Updates either the Overworld or the Arena depending on which one is active
        :param inputs: most recent input
        """
        if self.isOverworld:
            self.overworld.update(inputs)
        else:
            self.arena.update(inputs)

    def drawOverworld(self):
        """
            The Overworld is drawn and printed
        :param screen:
        """
        self.overworld.draw(self.screen)
        self.screen.print()

if __name__ == '__main__':

    # Run the game only if this module is run as the main program.
    game = Universe(160, 20)
    while (game.reset == True):
        game = Universe(160, 20)
