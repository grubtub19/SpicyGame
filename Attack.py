class Attack():
    def __init__(self, name, damage, hitChance, statusEffect=None):
        self.name = name
        self.damage = damage
        self.hitChance = hitChance
        self.statusEffect = statusEffect
