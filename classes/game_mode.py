from utils.string_helpers import compile_and_print_msg
from classes.game_option import (GameOption)

game_mode_msg = "\nSelected game mode is:"

class GameMode():
    game_options = [GameOption("1 vs 1", 1), GameOption("2 vs 2", 2), GameOption("5 vs 5", 5)]
    selected_option: GameOption = None

    def __init__(self):
        while self.selected_option == None:
            self.selected_option = prompt_game_mode(self.game_options)
        compile_and_print_msg([game_mode_msg, self.selected_option.description], True)

def prompt_game_mode(game_options: list[GameOption]):
    counter = 0
    for option in game_options:
        counter += 1
        print(str(counter) + ":", option.description)
    user_option_input = input("Please, select a game mode from the list by entering option number: ")
    if not user_option_input.isnumeric():
        return None
    elif int(user_option_input) > counter:
        return None
    else:
        return game_options[int(user_option_input) - 1]
