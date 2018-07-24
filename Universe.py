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

        f = open("sprites/startingScreen.txt", "r")
        startingScreen = f.read()
        print(startingScreen)
        self.textBox = TextBox(0,15)
        self.screen = Screen(self, screen_width, screen_height)
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.isOverworld = True  # False if the current stage is the Arena
        self.overworld = Overworld(
            self, width=40, height=11, overworld_x=60, overworld_y=4)

        self.player = Player(
            overworld_x=81, overworld_y=9,
            sprites_path="sprites/player.txt",
            overworldChar="P", arena_x=50, arena_y=10, defensePower=100, evade=0.2,
            health=2000, crit=0.2, moveset=[  # TODO: Balance these.
                Attack(name='Heavy Attack', damage=400, hitChance=0.95, statusEffect=StatusEffect(name="Spice", duration=6, damagePerTurn=6, sprite_path="sprites/spiceEffect.txt")),
                Attack(name='Regular Attack', damage=100, hitChance=0.6),
                Attack(name='Light Attack', damage=70, hitChance=0.6)
            ])
        # array containing all monsters
        self.monsters = [
            Monster(
                overworld_x=84, overworld_y=11,
                sprites_path='sprites/pepperSprite.txt',
                overworldChar="M", arena_x=30, arena_y=10, defensePower=20, health=2000, evade=0.2, crit=0.1,
                moveset=[  # TODO: Balance these.
                    Attack(name='Poison Attack', damage=300, hitChance=0.95,
                           statusEffect=StatusEffect(name="Poison", duration=3, damagePerTurn=20, sprite_path="sprites/poisonEffect.txt")),
                    Attack(name='Spice Attack', damage=75, hitChance=0.6,
                           statusEffect=StatusEffect(name="Spice", duration=6, damagePerTurn=6, sprite_path="sprites/spiceEffect.txt")),
                    Attack(name='Light Attack', damage=18, hitChance=0.6)
                ]),
            Monster(
                overworld_x=74, overworld_y=8,
                sprites_path='sprites/pepperSprite.txt',
                overworldChar="M", arena_x=30, arena_y=10, defensePower=20, health=1000, evade=0.2, crit=0.1,
                moveset=[  # TODO: Balance these.
                    Attack(name='Heavy Attack', damage=300, hitChance=0.95),
                    Attack(name='Regular Attack', damage=75, hitChance=0.6),
                    Attack(name='Light Attack', damage=18, hitChance=0.6)
                ]),
            Monster(
                overworld_x=88, overworld_y=8,
                sprites_path='sprites/pepperSprite.txt',
                overworldChar="M", arena_x=30, arena_y=10, defensePower=20, health=1000, evade=0.2, crit=0.1,
                moveset=[  # TODO: Balance these.
                    Attack(name='Heavy Attack', damage=300, hitChance=0.95),
                    Attack(name='Regular Attack', damage=75, hitChance=0.6),
                    Attack(name='Light Attack', damage=18, hitChance=0.6)
                ])
        ]

        self.playerHealthBar = HealthBar(self.player)

        self.healthpot = [
            HealthPot(overworld_x=78, overworld_y=11, overworldChar = "+", ASCII = ["+"], health = 150),
            HealthPot(overworld_x=84, overworld_y=7, overworldChar = "+", ASCII = ["+"], health = 150)
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