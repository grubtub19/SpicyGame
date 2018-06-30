class Overworld:

    def __init__(self, universe, x, y):
        self.universe = universe
        self.x = x
        self.y = y

    def update(self, inputs):
        self.universe.player.update(inputs)

    def draw(self, screen):
        for monster in self.universe.monsters:
            monster.drawOverworld(screen)

        # This is drawn last so the player is always 'on top' in relation
        # to other drawn objects.
        self.universe.player.drawOverworld(screen)
