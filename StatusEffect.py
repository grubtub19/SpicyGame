from Entity import *
import math
import copy


class StatusEffect():
    def __init__(self, name, duration, damagePerTurn, sprite_path):
        self.name = name
        self.duration = duration
        self.damagePerTurn = damagePerTurn
        self.icon = Entity(overworld_x=0, overworld_y=0, sprite="", overworldChar="", arena_x=0, arena_y=0)
        self.icon.setSprite(sprite_path)
        self.blankSprite = self.icon.sprite

    def updateSpriteDuration(self):
        tempSprite = copy.deepcopy(self.blankSprite)
        centerY = math.ceil((len(tempSprite) / 2) - 1)

        tempSprite[centerY] = tempSprite[centerY][:len(tempSprite[centerY]) - 8] + str(self.duration)\
                            + tempSprite[centerY][len(tempSprite[centerY]) - 8 + len(str(self.duration)):]
        self.icon.sprite = tempSprite

