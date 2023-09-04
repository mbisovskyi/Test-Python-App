from classes.combatant import Combatant
from classes.armor import Armor
from classes.weapon import Weapon

class Robot(Combatant):
    health = 100
    weapon = None
    armor = None

    def __init__(self, name):
        self.name = name
        self.my_type = "Robot"
        self.weapon = Weapon()
        self.attack_power = self.weapon.attack
        self.armor = Armor()