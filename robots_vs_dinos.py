from utils.string_helpers import compile_and_print_msg
from classes.game_mode import GameMode
from classes.battlefield import Battlefield
from classes.round import Round

greeting_msg = "\nThis is the greatest game ever created. We have spent 5 years to develope this beauty! SO PLAY IT!!!"

def run_robots_vs_dinos():
    # Print greeting message
    compile_and_print_msg([greeting_msg], True)
    # Prompt player to select Game Mode
    game_mode = GameMode()
    # Define battlefield
    battlefield = Battlefield()
    # Spawn combatants on the battlefield
    battlefield.generate_combatants(game_mode.selected_option.team_characters_count)
    # Start battle
    battlefield.start_battle()