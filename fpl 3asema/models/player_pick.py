class PlayerPick:
    def __init__(self, player_id, position,captain,vice_captain, multiplier=1):
        self.player_id = player_id
        self.position = position
        self.captain=captain
        self.vice_captain=vice_captain  
        self.multiplier = multiplier


    # def calculate_points(self):
    #     return self.player.gameweek * self.multiplier   
       