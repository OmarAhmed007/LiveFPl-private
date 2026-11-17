class PlayerGameweek:
    def __init__(
        self,
        player_id,
        fixture_id,
        gameweek,
        points,
        minutes,
        goals,
        assists,
        clean_sheets,
        bonus,
        ownership=0
    ):
        self.player_id = player_id
        self.fixture_id = fixture_id  # a double gameweek gives two rows with the same gameweek
        self.gameweek = gameweek
        self.ownership = ownership
        self.points = points
        self.minutes = minutes
        self.goals = goals
        self.assists = assists
        self.clean_sheets = clean_sheets
        self.bonus = bonus
