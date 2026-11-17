from api.data_mapper import DataMapper
from models.league import League


data_mapper = DataMapper()

# ---- Managers ---------------------------------------------------------------
managers = data_mapper.map_manager_data()
manager_dict = {manager.id: manager for manager in managers}

# ---- League -----------------------------------------------------------------
# A league doesn't hold its managers; membership is a separate list of
# (league_id, manager_id) pairs (the same idea as a link table in a database).
league = League(id=1, name="My League")
league_managers = [(league.id, manager.id) for manager in managers]

# ---- Players ----------------------------------------------------------------
players = data_mapper.map_player_data()
players_dict = {player.id: player for player in players}

# player_id -> list of PlayerGameweek
player_gameweeks = {}
for player in players:
    player_gameweeks[player.id] = data_mapper.map_player_gameweek_data(player.id)

# ---- Manager gameweeks and picks --------------------------------------------
# manager_id -> list of ManagerGameweek
manager_gameweeks = {}
# (manager_id, gameweek) -> list of PlayerPick
player_picks = {}

for manager_id in manager_dict:
    manager_gameweeks[manager_id] = data_mapper.map_manager_gameweek_history(manager_id)

    # Only the gameweeks this manager actually played
    for manager_gameweek in manager_gameweeks[manager_id]:
        gw = manager_gameweek.gameweek
        player_picks[(manager_id, gw)] = data_mapper.map_playerPick_history(manager_id, gw)

# ---- Quick look at the result -----------------------------------------------
for (manager_id, gw), picks in player_picks.items():
    captain = next((pick for pick in picks if pick.captain), None)
    captain_name = players_dict[captain.player_id].first_name+" "+players_dict[captain.player_id].last_name if captain else "-"
    print(f"{manager_dict[manager_id].team_name} | GW{gw} | captain: {captain_name}")
