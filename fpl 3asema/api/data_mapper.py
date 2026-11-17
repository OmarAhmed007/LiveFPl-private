from api.fpl_api import APIManager
from models.manager import Manager
from models.player import Player
from models.player_gameweek import PlayerGameweek
from models.manager_gameweek import ManagerGameweek
from models.player_pick import PlayerPick


class DataMapper:
    def __init__(self):
        self.api_manager = APIManager()

    def map_manager_data(self):
        manager_IDS = [69432, 31849, 115677, 4341577, 192746, 4069899, 44702, 8370833, 7997442, 7014791]
        managers = []

        for manager_id in manager_IDS:
            manager_data = self.api_manager.get_manager_data(manager_id)
            if not manager_data:
                print(f"Skipping manager {manager_id}: no data returned")
                continue

            manager = Manager(
                id=manager_data["id"],
                first_name=manager_data["player_first_name"],
                last_name=manager_data["player_last_name"],
                team_name=manager_data["name"],
            )
            managers.append(manager)
        return managers

    def map_player_data(self):
        players = self.api_manager.get_player_data()
        if players is None:
            print("Could not load player data")
            return []

        players_list = []
        for player in players:
            pl = Player(
                id=player["id"],
                first_name=player["first_name"],
                last_name=player["second_name"],
                position=player["element_type"],
            )
            players_list.append(pl)
        return players_list

    def map_player_gameweek_data(self, player_id):
        player_gameweek_history = self.api_manager.get_player_gameweek_data(player_id)
        if player_gameweek_history is None:
            print(f"No gameweek data for player {player_id}")
            return []

        pl_gameweek_history = []
        for player_gameweek in player_gameweek_history:
            pl_gameweek = PlayerGameweek(
                player_id=player_id,
                fixture_id=player_gameweek["fixture"],
                gameweek=player_gameweek["round"],
                points=player_gameweek["total_points"],
                minutes=player_gameweek["minutes"],
                goals=player_gameweek["goals_scored"],
                assists=player_gameweek["assists"],
                clean_sheets=player_gameweek["clean_sheets"],
                bonus=player_gameweek["bonus"],
            )
            pl_gameweek_history.append(pl_gameweek)

        return pl_gameweek_history

    def map_manager_gameweek_history(self, managerId):
        manager_gameweek = self.api_manager.get_manager_gameweek_history(manager_id=managerId)
        if manager_gameweek is None:
            print(f"No gameweek history for manager {managerId}")
            return []

        mg_gameweek_history = []
        for x in manager_gameweek.get("current", []):
            mg_gameweek = ManagerGameweek(
                manager_id=managerId,
                gameweek=x["event"],
                points=x["points"],
                total_points=x["total_points"],
                rank=x["overall_rank"],
                team_value=x["value"],
                bank_value=x["bank"],
            )
            mg_gameweek_history.append(mg_gameweek)

        return mg_gameweek_history

    def map_playerPick_history(self, manager_id, gameweek):
        playerPick_gameweek = self.api_manager.get_playerPick_history(manager_id, gameweek)
        if playerPick_gameweek is None:
            # Expected for gameweeks the manager didn't play (or not yet played)
            return []

        pl_pick_gameweek_history = []
        for x in playerPick_gameweek.get("picks", []):
            pl_pick_gameweek = PlayerPick(
                manager_id=manager_id,
                gameweek=gameweek,
                player_id=x["element"],
                position=x["position"],
                captain=x["is_captain"],
                vice_captain=x["is_vice_captain"],
                multiplier=x["multiplier"],
            )
            pl_pick_gameweek_history.append(pl_pick_gameweek)
        return pl_pick_gameweek_history
