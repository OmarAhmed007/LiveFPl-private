class ManagerGameweek:
    def __init__(
        self,
        manager_id,
        gameweek,
        points,
        total_points,
        rank,
        team_value,
        bank_value
    ):
        self.manager_id = manager_id
        self.gameweek = gameweek
        self.points = points
        self.total_points = total_points
        self.rank = rank
        self.team_value = team_value
        self.bank_value = bank_value
