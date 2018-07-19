from Entity import *


class TextBox(Entity):
    def __init__(self, x, y):
        """
        A textBox is an Entity that only uses the Arena position and sprite. Overworld variable are never used. Always call textBox.drawArena()
        :param x:
        :param y:
        """
        Entity.__init__(self, overworld_x=0, overworld_y=0, sprite=["ojas","alsndkn","asldjf"], overworldChar=[], arena_x=x, arena_y=y)
        self.blankSprite = ["------------------------",
                 "|                      |",
                 "|                      |",
                 "|                      |",
                 "------------------------"]
        self.sprite = self.blankSprite
        self.text = ["hi bob","string",""]
        self.height = 3

    def print(self, string):
        self.text.insert(0,string)
        self.text.pop(self.height)

    def drawBox(self, screen):
        """
        DONT TOUCH. IDK HOW IT WORKS ANYMORE
        """
        self.sprite = self.blankSprite
        for i in range(0, len(self.text)):
            self.sprite[self.height-i] = self.sprite[self.height-i][:2] + self.text[i] + self.sprite[self.height-i][len(self.text[i])+2:]
            """for j in range(0, len(self.text[i])):
                self.sprite[self.height-i] = self.sprite[self.height-i][:j+2] + self.text[i][j] + self.sprite[self.height-i][j+3:]
                if j > len(self.sprite[0]) - 6:
                    break"""
        self.drawArena(screen)

        #TODO: self.wipe():
