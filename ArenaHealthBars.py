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
        monsterBarNum = ceil(ArenaHealthBars.barLength \
            * self.monster.currentHealth / self.monster.maxHealth)

        del_dot_1 = len("Health: " + str(self.player.currentHealth)) #counts number of characters
        del_dot_2 = len("Health: " + str(self.monster.currentHealth))

        for i in range(0, playerBarNum):
            screen.buffer[1][i] = '**' # print player healthbar in top left corner
            del screen.buffer[1][-1]

        if (self.player.maxHealth != self.player.currentHealth):
            for k in range(playerBarNum, ArenaHealthBars.barLength):
                screen.buffer[1][k] = '--'
                del screen.buffer[1][-1]

        screen.buffer[1][ArenaHealthBars.barLength] = "|"

        screen.buffer[0][0] = "Health: " + str(self.player.currentHealth) #gives health points

        for i in range(0, del_dot_1-1):
            del screen.buffer[0][-1] #deletes characters at end of the line to keep same dimensions

        for j in range(len(screen.buffer[0]), len(screen.buffer[0]) - monsterBarNum, -1):
            screen.buffer[len(screen.buffer)-1][j] = '**'
            del screen.buffer[len(screen.buffer)-1][-1]

        if (self.monster.maxHealth != self.monster.currentHealth):
            for k in range(monsterBarNum, ArenaHealthBars.barLength,-1):
                screen.buffer[len(screen.buffer)-1][-k] = '--'
                del screen.buffer[len(screen.buffer)-1][-1]

        for i in range(0, del_dot_2-1):
            del screen.buffer[len(screen.buffer) - 2][-1] #deletes characters at end of the line to keep same dimensions

        screen.buffer[len(screen.buffer) - 1][-11] = "|"

        screen.buffer[len(screen.buffer) - 2][-12] = "Health: " + str(self.monster.currentHealth) #gives health points
