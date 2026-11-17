class PlayerPick:
    def __init__(self, manager_id, gameweek, player_id, position, captain, vice_captain, multiplier=1):
        self.manager_id = manager_id
        self.gameweek = gameweek
        self.player_id = player_id
        self.position = position
        self.captain = captain
        self.vice_captain = vice_captain
        self.multiplier = multiplier
