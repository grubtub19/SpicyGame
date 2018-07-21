from Pokemon import *


class Monster(Pokemon):
    def __init__(self, overworld_x, overworld_y, sprites_path, overworldChar, arena_x, arena_y, defensePower, health, evade, crit, moveset):
        Pokemon.__init__(self, overworld_x, overworld_y, sprites_path,
                         overworldChar, arena_x, arena_y, defensePower, health, evade, crit, moveset)
        self.statusUI = StatusEffectUI(self, False)
        self.damageText.moveInArena(115, 3)

    def drawArena(self, screen):
        Entity.draw(self, screen, self.sprite, self.arena_x, self.arena_y)
        self.statusUI.draw(screen)
