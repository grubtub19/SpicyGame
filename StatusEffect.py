from Entity import *


class StatusEffect():
    def __init__(self, name, duration, damagePerTurn, sprite_path):
        self.name = name
        self.duration = duration
        self.damagePerTurn = damagePerTurn
        self.icon = Entity(overworld_x=0, overworld_y=0, sprite="", overworldChar="", arena_x=0, arena_y=0)
        self.icon.setSprite(sprite_path)
