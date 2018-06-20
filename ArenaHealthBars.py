class ArenaHealthBars:
    barLength = 10

    def __init__(self, player, monster):
        self.player = player  # we extract health data from these
        self.monster = monster

    def draw(self, screen):
        barNum = ArenaHealthBars.barLength * int(round(self.player.currentHealth/self.player.maxHealth))  # calculate how many characters make up the healthbar
        for i in range(0, barNum):
            screen[0][i] = "X" # print player healthbar in top left corner
