from math import ceil

class ArenaHealthBars:
    barLength = 10

    def __init__(self, player, monster):
        # We extract health data from these.
        self.player = player
        self.monster = monster

    def draw(self, screen):
        # Calculate how many characters make up the healthbar.
        playerBarNum = ceil(ArenaHealthBars.barLength \
            * self.player.currentHealth / self.player.maxHealth)
        monsterBarNum = ceil(ArenaHealthBars.barLength
            * self.monster.currentHealth / self.monster.maxHealth)

        for i in range(0, playerBarNum):
            screen.buffer[0][i] = '#' # print player healthbar in top left corner

        for j in range(len(screen.buffer[0]) - 1, len(screen.buffer[0]) - 1 - monsterBarNum, -1):
            screen.buffer[len(screen.buffer) - 1][j] = '#'
