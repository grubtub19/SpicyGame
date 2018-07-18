from Entity import *
import random

class Pokemon(Entity):
    """
        Any Entity that can battle is a Pokemon (Player, Monster)
    """

    def __init__(self, overworld_x, overworld_y, sprites_path, overworldChar, arena_x, arena_y, defensePower, health,  crit, moveset):
        self.neutralSprite = []
        self.startAttackSprite = []
        self.endAttackSprite = []
        self.flinchSprite = []

        self.loadSprites(sprites_path)

        Entity.__init__(self, overworld_x, overworld_y, self.neutralSprite, overworldChar, arena_x, arena_y)
        self.defensePower = defensePower
        self.maxHealth = health
        self.currentHealth = health
        self.crit = crit
        self.moveset = moveset

    def attack(self, attack, target):
        #  Calculate damage.
        # damage = att * att / (att + def)
        # https://gamedev.stackexchange.com/questions/129319/rpg-formula-attack-and-defense
        damage = int(attack.damage * attack.damage / (
            attack.damage + target.defensePower))
        # implrment critical chance and damage
        prob = random.randint(0, 100) / 100
        if prob <= self.crit:
            print("we crit")
            damage = damage * 1.5
        print(damage)
        #  Apply damage to monster.
        target.currentHealth -= damage

    def loadSprites(self, filename):
        """Loads sprites from a .txt file and assigns them to Pokemon's attributes.

        Assumes that each sprite in the .txt file is delimited by an empty line.
        """
        sprites = []

        with open(filename) as f:
            sprite = []
            for line in f:
                sprite.append(line.rstrip())
                if line == '\n':
                    # Delimit on empty lines.
                    del sprite[-1]
                    sprites.append(sprite)
                    sprite = []
            # The last \n in the file doesn't seem to show, so
            # here's a hack around that.
            sprites.append(sprite)

        self.neutralSprite = sprites[0]
        self.startAttackSprite = sprites[1]
        self.endAttackSprite = sprites[2]
        self.flinchSprite = sprites[3]
