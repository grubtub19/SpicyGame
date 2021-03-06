from Entity import *
from Player import *
from Monster import *
from math import ceil

class Stats:

    @staticmethod
    def WriteFile(path, universe):
        f = open('%s.txt' % path, "w")
        f.write("Name: " + path)
        f.write("\n\t\tSCORE: " + str(universe.score) + "\n\n")
        f.write("Total damage inflicted: " + str(universe.damageInflicted) + "\n")
        f.write("Total damage received: " + str(universe.damageReceived) + "\n")
        f.close()
