class ManagerGameweek:
    def __init__(
        self,
        gameweek,
        points,
        total_points,
        rank,
        team_value,
        bank_value,
        players_list=None
    ):
        self.gameweek = gameweek
        self.points = points
        self.total_points = total_points
        self.rank = rank
        self.team_value = team_value
        self.bank_value = bank_value
        self.players_list = players_list if players_list is not None else []