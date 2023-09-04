from classes.robot import Robot
from classes.dino import Dino

class Round:
    instances_count = 0
    title = ""

    def __init__(self):
        Round.instances_count += 1
        self.title = "Round " + str(self.instances_count)
