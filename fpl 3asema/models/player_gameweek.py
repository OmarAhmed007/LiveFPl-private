class PlayerGameweek:
    def __init__(
        self,
        gameweek,
        points,
        minutes,
        goals,
        assists,
        clean_sheets,
        bonus,
        ownership=0
    ):
        self.gameweek = gameweek
        self.ownership = ownership
        self.points = points
        self.minutes = minutes
        self.goals = goals
        self.assists = assists
        self.clean_sheets = clean_sheets
        self.bonus = bonus