from Entity import *
from Player import *
from Monster import *
from math import ceil

class HealthBar(Entity):
    barLength = 10

    def __init__(self, owner):
        # Pointer to the health bar's owner.
        self.owner = owner

        # Assign Overworld and Arena sprites.
        if isinstance(owner, Player):
            self.overworld_x, self.overworld_y = 0, 0
            self.arena_x, self.arena_y = 0, 0
        elif isinstance(owner, Monster):
            # TODO: Find a way not to hardcode the Arena coordinates.
            self.overworld_x, self.overworld_y = 0, 0
            self.arena_x, self.arena_y = 138, 18

        Entity.__init__(self,
            overworld_x=self.overworld_x, overworld_y=self.overworld_y,
            sprite=[], overworldChar=[], arena_x=self.arena_x, arena_y=self.arena_y
        )

    def drawSprite(self, owner):
        finalSprite = []

        # Calculate how many characters make up the healthbar.
        barNum = ceil(self.barLength
                      * self.owner.currentHealth / self.owner.maxHealth)

        # Start with showing the numerical value.
        finalSprite = ['Health: %s' % self.owner.currentHealth]

        # Draw Arena sprite.
        healthBarSprite = ""

        # Draw bars representing health left.
        for _ in range(0, barNum):
            healthBarSprite += '**'

        # Draw bars representing health missing.
        for _ in range(0, self.barLength - barNum):
            healthBarSprite += '--'

        # Draw end of health bar.
        healthBarSprite += '|'

        # Sprite complete.
        finalSprite.append(healthBarSprite)

        if isinstance(owner, Monster):
            finalSprite[0] = ' ' * 9 + finalSprite[0]

            # Reverse the health bar sprite.
            # https://stackoverflow.com/questions/931092/reverse-a-string-in-python
            finalSprite[1] = finalSprite[1][::-1]

        return finalSprite


    def drawArena(self, screen):
        self.sprite = self.drawSprite(self.owner)
        super().drawArena(screen)

    def drawOverworld(self, screen):
        self.overworldChar = self.drawSprite(self.owner)
        super().drawOverworld(screen)
