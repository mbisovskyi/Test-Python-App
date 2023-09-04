import random

class Armor:
    name = ""
    armor = 0

    def __init__(self):
        armor_names_list = ["Silky Robe",
                            "Wooden Defense",
                            "Metal Gear"]
        max_armor_limit = 50
        min_armor_limit = 10

        self.name = random.choice(armor_names_list)
        self.armor = random.randint(min_armor_limit, max_armor_limit)
