import random

class Weapon:
    name = ""
    attack = 0
    penetration = 0

    def __init__(self):
        min_attack_limit = 10
        max_attack_limit = 50
        min_penetration_limit = round((min_attack_limit * 0.2))
        max_penetration_limit = round((max_attack_limit * 0.2))
        weapon_names_list = ["Light Sabre", 
                             "Chain Saw", 
                             "Metal Feasts", 
                             "Energy Beams"]

        self.name = random.choice(weapon_names_list)
        self.attack = random.randint(min_attack_limit, max_attack_limit)
        self.penetration = random.randint(min_penetration_limit, max_penetration_limit)