from Entity import *
from Player import *
from Monster import *
from math import ceil

class Stats:
    
    def __init__(self, path):
        self.path = path
    
    @staticmethod    
    def WriteFile(path, universe, name):
        f = open(path, "w")
        f.write("\n" + name)
        f.write("\n\t\tSCORE: " + str(universe.score) + "\n\n")
        f.write("Total damage inflicted: " + str(universe.damageInflicted) + "\n")
        f.write("Total damage received: " + str(universe.damageReceived) + "\n")
        f.close()
        
        

        
        