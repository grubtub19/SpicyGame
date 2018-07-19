from Entity import *
import random
import copy

class Pokemon(Entity):
    """
        Any Entity that can battle is a Pokemon (Player, Monster)
    """
    critMultiplier = 1.5

    def __init__(self, overworld_x, overworld_y, sprites_path, overworldChar, arena_x, arena_y, defensePower, health, evade, crit, moveset):
        self.neutralSprite = []
        self.startAttackSprite = []
        self.endAttackSprite = []
        self.flinchSprite = []

        self.loadSprites(sprites_path)

        Entity.__init__(self, overworld_x, overworld_y, self.neutralSprite, overworldChar, arena_x, arena_y)
        self.defensePower = defensePower
        self.maxHealth = health
        self.currentHealth = health
        self.evade = evade
        self.crit = crit
        self.moveset = moveset
        self.nextAttackDamage = 0
        self.nextAttackCrits = False
        self.nextAttackHits = True
        self.currStatusEffects = []

    def calcHit(self, attack, target):
        """
        Calculate dodge. Saves it to self.nextAttackHits
        """
        finalHitChance = attack.hitChance * (1 - target.evade)
        prob = random.randint(0, 100) / 100
        if finalHitChance >= prob:
            self.nextAttackHits = True


    def calcDamage(self, attack, target):
        """
        Calculates damage and crit. Saves it to self.nextAttackDamage and self.nextAttackCrits
        """
        damage = int(attack.damage * attack.damage / (attack.damage + target.defensePower))

        # critical chance calculations
        prob = random.randint(0, 100) / 100
        if self.crit >= prob:
            self.nextAttackCrits = True
            damage = damage * Pokemon.critMultiplier
        self.nextAttackDamage = damage

    def calcAttack(self, attack, target):
        #  Calculate damage that is to be applied to the target in the future.
        # damage = att * att / (att + def)
        # https://gamedev.stackexchange.com/questions/129319/rpg-formula-attack-and-defense
        self.nextAttackHits = False
        self.nextAttackCrits = False
        self.nextAttackDamage = 0

        self.calcHit(attack, target)
        if self.nextAttackHits:
            self.calcDamage(attack, target)

    def applyAttack(self, attack, target):
        #  Apply damage to monster.
        if self.nextAttackHits:
            target.currentHealth -= self.nextAttackDamage
            if attack.statusEffect != None:
                self.addStatusEffect(attack.statusEffect, target)
            else:
                print("did not add effect")

    def addStatusEffect(self, statusEffect, target):
        print("added status effect " + statusEffect.name)
        target.currStatusEffects.append(copy.deepcopy(statusEffect))

    def applyStatusEffects(self):
        """
        Selects the most damaging effect of each effect type and applies it. Decrements each effect's duration, and removes any that reach 0.
        :return:
        """
        appliedEffects = [] # since we only want to apply each status effect type once, we keep track of which ones we've already applied
        toRemove = [] # keep track of all the effects who's duration has become 0 so we can remove them afterward
        for effect in self.currStatusEffects:
            mostDamagingEffect = effect
            # check if we've already applied the damage of the current effect type
            if effect.name not in appliedEffects:

                appliedEffects.append(effect.name)
                # ideally we would want to iterate from the current position in self.currStatusEffects onward, but
                # doing it this was makes it simpler
                for otherEffect in self.currStatusEffects:

                    if otherEffect.name == effect.name and otherEffect.damagePerTurn > mostDamagingEffect.damagePerTurn:
                        otherEffect = mostDamagingEffect #compares all effects of the same type and finds the most damaging
                self.currentHealth -= mostDamagingEffect.damagePerTurn
                print("Applied " + str(mostDamagingEffect.damagePerTurn) + " damage of type " + mostDamagingEffect.name)

            effect.duration -= 1
            if effect.duration <= 0:
                toRemove.append(effect)

        for item in toRemove:
            print("removed " + item.name + " from effects list")
            self.currStatusEffects.remove(item)



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
