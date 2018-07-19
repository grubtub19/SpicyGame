from Overworld import *
from Player import *
from Monster import *
from Arena import *
from Screen import *
from Attack import *
from StatusEffect import *
from TextBox import *
from HealthPot import *


class Universe:
    """
        All of the Entities are stored here and are used in either Overworld or Arena depending on what stage is currently active
    """
    controls = ['w','a','s','d']

    def __init__(self, screen_width, screen_height):
        self.textBox = TextBox(0,13)
        self.screen = Screen(self, screen_width, screen_height)
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.isOverworld = True  # False if the current stage is the Arena
        self.overworld = Overworld(
            self, width=40, height=15, overworld_x=60, overworld_y=1)

        # Pulled Player ASCII art from http://www.ascii-art.de/ascii/s/stickman.txt
        # (Darth Vader and Luke go at it!)
        self.player = Player(
            overworld_x=80, overworld_y=9,
            sprites_path="player.txt",
            overworldChar="P", arena_x=50, arena_y=10, defensePower=100, evade=0.2,
            health=1000, crit=0.2, moveset=[  # TODO: Balance these.
                Attack(name='Heavy Attack', damage=400, hitChance=0.6),
                Attack(name='Regular Attack', damage=100, hitChance=0.6),
                Attack(name='Light Attack', damage=70, hitChance=0.6)
            ])
        # array containing all monsters
        self.monsters = [
            Monster(
                overworld_x=81, overworld_y=10,
                sprites_path='PepperSprite.txt',
                overworldChar="M", arena_x=30, arena_y=10, defensePower=20, health=1000, evade=0.2, crit=0.1,
                moveset=[  # TODO: Balance these.
                    Attack(name='Poison Attack', damage=300, hitChance=1.0,
                           statusEffect=StatusEffect(name="Poison", duration=3, damagePerTurn=20, sprite_path="poisonEffect.txt")),
                    Attack(name='Spice Attack', damage=75, hitChance=0.6,
                           statusEffect=StatusEffect(name="Spice", duration=6, damagePerTurn=6, sprite_path="spiceEffect.txt")),
                    Attack(name='Light Attack', damage=18, hitChance=0.6)
                ]),
            Monster(
                overworld_x=70, overworld_y=5,
                sprites_path='PepperSprite.txt',
                overworldChar="M", arena_x=30, arena_y=10, defensePower=20, health=1000, evade=0.2, crit=0.1,
                moveset=[  # TODO: Balance these.
                    Attack(name='Heavy Attack', damage=300, hitChance=0.6),
                    Attack(name='Regular Attack', damage=75, hitChance=0.6),
                    Attack(name='Light Attack', damage=18, hitChance=0.6)
                ]),
            Monster(
                overworld_x=74, overworld_y=8,
                sprites_path='pepperSprite.txt',
                overworldChar="M", arena_x=30, arena_y=10, defensePower=20, health=1000, evade=0.2, crit=0.1,
                moveset=[  # TODO: Balance these.
                    Attack(name='Heavy Attack', damage=300, hitChance=0.6),
                    Attack(name='Regular Attack', damage=75, hitChance=0.6),
                    Attack(name='Light Attack', damage=18, hitChance=0.6)
                ])
        ]

        self.healthpot = [
            HealthPot(overworld_x=70, overworld_y=4, overworldChar = "+", ASCII = ["+"], health = 150),
            HealthPot(overworld_x=84, overworld_y=7, overworldChar = "+", ASCII = ["+"], health = 150)
        ]

        self.arena = None  # we use startArena() to instantiate this
        self.loop()

    def startArena(self, monsterIndex):
        """
            Instantiates the arena against a monster and changes the stage
        :param monster:
        """
        self.isOverworld = False
        self.arena = Arena(self, self.player, monsterIndex)

    def loop(self):
        while(True):
            # TODO: Add title screen.
            self.update(self.getInputs())
            self.draw(self.screen)

    def getInputs(self):
        return input('>> ')

    def update(self, inputs):
        """
            updates either the Overworld or the Arena depending on which one is active
        :param inputs: most recent input
        """
        if self.isOverworld:
            self.overworld.update(inputs)
        else:
            self.arena.update(inputs)

    def draw(self, screen):
        """
            The screen is drawn using the Overworld or the Arena's draw() function
        :param screen:
        """
        if self.isOverworld:
            self.overworld.draw(screen)
        else:
            self.arena.draw(screen)
        screen.print()

if __name__ == '__main__':
    f = open("startingscreen.txt", "r")
    startingScreen = f.read()
    print(startingScreen)
    # Run the game only if this module is run as the main program.
    game = Universe(160, 20)
