from Entity import *
import copy
import math

class StatusEffectUI:

    def __init__(self, pokemon, left):
        self.pokemon = pokemon
        self.left = left
        self.visibleEffects = []
        self.damageIsShown = False

    def decrementAndRemove(self):
        toRemove = []
        for vEffect in self.visibleEffects:
            if vEffect.duration <= 0:
                toRemove.append(vEffect)

        for item in toRemove:
            self.visibleEffects.remove(item)

    def updateVisibleEffects(self):

        self.decrementAndRemove()

        for cEffect in self.pokemon.currStatusEffects:
            found = False
            for vEffect in self.visibleEffects:
                if vEffect.name == cEffect.name:
                    found = True
                    if cEffect.duration > vEffect.duration:
                        vEffect.duration = cEffect.duration

            if not found:
                self.visibleEffects.append(cEffect)

    def draw(self, screen):
        self.updateVisibleEffects()
        for index, effect in enumerate(self.visibleEffects):
            if self.left:
                effect.updateSpriteDuration()
                effect.icon.moveInArena(0, 2 + (5 * index))
                if self.damageIsShown:
                    damage = Entity(0, 0, [str(effect.damagePerTurn)], "", len(effect.icon.sprite[0]) + 6, 4 + (5 * index))
                    damage.drawArena(screen)
            else:
                effect.updateSpriteDuration()
                effect.icon.moveInArena(139, 2 + (5 * index))
                if self.damageIsShown:
                    damage = Entity(0, 0, [str(effect.damagePerTurn)], "", 132, 4 + (5 * index))
                    damage.drawArena(screen)
            effect.icon.drawArena(screen)
        self.damageIsShown = False