from utils.string_helpers import compile_and_print_msg

class Combatant:
    name = ""
    attack_power = ""
    my_type = ""

    def do_attack(self, enemy):
        enemy.health -= self.attack_power
        compile_and_print_msg([self.name, "attacks", enemy.name, "and deals", str(self.attack_power), "of damage."], True)
        compile_and_print_msg([enemy.name, "remains with", str(enemy.health), "of health points."], True)
