from Entity import *
import random

class Pokemon(Entity):
    """
        Any Entity that can battle is a Pokemon (Player, Monster)
    """

    def __init__(self, overworld_x, overworld_y, ASCII, overworldChar, arena_x, arena_y, defensePower, health,  crit, moveset):
        Entity.__init__(self, overworld_x, overworld_y, ASCII, overworldChar, arena_x, arena_y)
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
