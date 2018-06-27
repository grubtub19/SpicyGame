from Player import *
import curses

class Game:
    """ The Game World contains methods for printing each frame and contains everything in the game world"""
    controls = [['w','a','s','d'],['i','j','k','l']]

    def __init__(self,x,y,playerCount):
        """ Create new game with """
        self.field = []
        self.initField(10,10)
        self.players = []
        self.players.append(Player(self,5,2))
        self.players.append(Player(self,5,8))
        self.players[0].setControls(Game.controls[0])
        self.players[1].setControls(Game.controls[1])
        self.stdscr = curses.initscr()

    def initField(self,x,y):
        for i in range(0,x):
            self.field.append([])
            for j in range(0,y):
                self.field[i].append('.')

    def getInput(self):
        hasInput = []
        for i in range(len(self.players)):
            hasInput.append(0)
        for j in range(0,len(self.players)):
            while(self.calcTotalInputs(hasInput) < j + 1):
                inputStr = self.stdscr.getch()
                for playerNum in range(0,len(self.players)):
                    if(hasInput[playerNum] == 0):
                        if(inputStr in self.players[playerNum].controls):
                            self.players[playerNum].setInput(inputStr)
                            hasInput[playerNum] = 1

    def calcTotalInputs(self, hasInput):
         totalInputs = 0
         for i in hasInput:
            totalInputs = totalInputs + i
         return totalInputs

    def update(self):
        self.getInput()
        for player in self.players:
            player.update()

    def print(self):
        self.wipeFrame()
        for player in self.players:
            player.printPlayer()
        self.printFrame()

    def wipeFrame(self):
        for i in range(0,len(self.field)):
            for j in range(0,len(self.field[i])):
                self.field[i][j] = '.'

    def printFrame(self):
        for i in self.field:
            for j in i:
                print(j, end='')
            print()

    def play(self):
        while(1):
            self.update()
            self.print()

