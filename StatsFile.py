from Entity import *
from Player import *
from Monster import *
from math import ceil

class Stats:
    
    def __init__(self, path):
        self.path = path
        
    def WriteFile(self, path):
        f = open(path, "w")
        f.write("SCORE: " + str(self.universe.score) + "\n")
        f.write("Total damage inflicted: " + str(self.universe.damageInflicted) + "\n")
        f.write("Total damage received: " + str(self.universe.damageReceived) + "\n")
        f.close()
        
        

        
        