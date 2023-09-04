class GameOption:
    type = "GameOption"
    description = ""
    team_characters_count = 0

    def __init__(self, description, team_characters_count):
        self.description = description
        self.team_characters_count = team_characters_count
    