from Entity import *
import random

class Pokemon(Entity):
    """
        Any Entity that can battle is a Pokemon (Player, Monster)
    """
    def __init__(self, overworld_x, overworld_y, ASCII, overworldChar, attackPower, defensePower, health, arena_x, arena_y, crit):
        Entity.__init__(self, overworld_x, overworld_y, ASCII, overworldChar, arena_x, arena_y)
        self.attackPower = attackPower
        self.defensePower = defensePower
        self.maxHealth = health
        self.currentHealth = health
        self.crit = crit

    def attack(self, monster):
        #  Calculate damage.
        # damage = att * att / (att + def)
        # https://gamedev.stackexchange.com/questions/129319/rpg-formula-attack-and-defense
        damage = int(self.attackPower * self.attackPower / (
            self.attackPower + monster.defensePower))
        # implrment critical chance and damage
        prob = random.randint(0, 100)
        if prob <= self.crit:
            print("we crit")
            damage = damage * 1.5
        print(damage)
        #  Apply damage to monster.
        monster.currentHealth -= damage
        
    def monsterAttack(self, player):
        #  Calculate damage.
        # damage = att * att / (att + def)
        # https://gamedev.stackexchange.com/questions/129319/rpg-formula-attack-and-defense
        damage = int(self.attackPower * self.attackPower / (
            self.attackPower + player.defensePower))
        # implrment critical chance and damage
        prob = random.randint(0, 100)
        if prob <= self.crit:
            print("we crit")
            damage = damage * 1.5
        print(damage)
        #  Apply damage to player.
        player.currentHealth -= damage