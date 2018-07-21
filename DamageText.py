from Entity import *

class DamageText(Entity):
    def __init__(self, arena_x, arena_y):
        Entity.__init__(self, 0, 0, "", "", arena_x, arena_y)

    def setText(self, damageNum, crit, statusEffect=None):
        string = [str(damageNum)]
        if crit:
            string[0] += " CRIT"
        if statusEffect is not None:
            string.append(statusEffect.name)
        self.sprite = string
        print("DamageText set to: " + str(self.sprite))

    def setMiss(self):
        self.sprite = ["MISS"]