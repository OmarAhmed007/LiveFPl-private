class Player:
    def __init__(self, id, first_name, last_name, position):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

        self.gameweeks=[]


    def get_player_gameweeks(self, data_mapper):
        self.gameweeks = data_mapper.map_player_gameweek_data(self.id)
        
            

