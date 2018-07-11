class StatusEffect():
    def __init__(self, name, turnsLeft, damagePerTurn, ASCII=None):
        self.name = name
        self.turnsLeft = turnsLeft
        self.damagePerTurn = damagePerTurn
        self.ASCII = ASCII
