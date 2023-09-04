import random
from utils.string_helpers import compile_and_print_msg
from classes.robot import Robot
from classes.dino import Dino
from classes.round import Round

battlefield_defined_msg = "\nChosen battlefield is:"

class Battlefield:
    name = ""
    robots = []
    dinos = []

    def __init__(self):
        battlefield_names_list = ["Stones Creek",
                                  "Walmart Register",
                                  "Airplane"]
        self.name = random.choice(battlefield_names_list)
        compile_and_print_msg([battlefield_defined_msg, self.name], True)

    
    def generate_combatants(self, characters_in_team: int):
        for character_number in range(characters_in_team):
            robot_name = prompt_combatant_name(character_number, "robot")
            self.robots.append(Robot(robot_name))
            dino_name = prompt_combatant_name(character_number, "dino")
            self.dinos.append(Dino(dino_name))
        compile_and_print_msg([compile_teams_info(characters_in_team, self.robots, self.dinos)], True)
    
    def start_battle(self):
        while not len(self.robots) <= 0 and not len(self.dinos) <= 0:
            round = Round()
            print(round.title)
            team_starts_first = determine_who_starts_first(["Robot", "Dino"])
            if team_starts_first == "Robot":
                attacker = self.robots[0]
                enemy = self.dinos[0]
            else:
                attacker = self.dinos[0]
                enemy = self.robots[0]
            attacker.do_attack(enemy)

            #Temporarily cuts off an infinite loop of while
            if round.instances_count == 3:
                self.robots.clear()

    
    
def prompt_combatant_name(combatant_number: int, combatant_type: str):
    input_msg = compile_and_print_msg(["Enter", str(combatant_number + 1), combatant_type + "'s name: "], False)
    name_input = input(input_msg)
    return name_input

def compile_teams_info(team_count: int, robots: list[Robot], dinos: list[Dino]):
    teams_info = "\nRobots:\n"
    for number in range(team_count):
        teams_info += "- " + compile_combatant_info(str(number + 1), robots[number]) + "\n"
    
    teams_info += "\nDinos:\n"
    for number in range(team_count):
        teams_info += "- " + compile_combatant_info(str(number + 1), dinos[number]) + "\n"
    return teams_info

def compile_combatant_info(combatant_number: int, combatant: Robot | Dino):
    if isinstance(combatant, Robot):  
        return compile_and_print_msg([combatant_number + ".", combatant.name + ";", "Weapon:", combatant.weapon.name + ";", "Armor:", combatant.armor.name], False)
    else:
        return compile_and_print_msg([combatant_number + ".", combatant.name], False)

def determine_who_starts_first(options: list[str]):
    return random.choice(options)