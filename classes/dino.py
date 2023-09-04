import random
from classes.combatant import Combatant

class Dino(Combatant):
    health = 125
    skin_thikness = 0

    def __init__(self, name):
        min_attack_power = 15
        max_attack_power = 65
        min_skin_thickness = 20
        max_skin_thickness = 60

        self.name = name
        self.my_type = "Dino"
        self.attack_power = random.randint(min_attack_power, max_attack_power)
        self.skin_thikness = random.randint(min_skin_thickness, max_skin_thickness)