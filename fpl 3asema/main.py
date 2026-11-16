from api.data_mapper import DataMapper

import requests



data_mapper=DataMapper()

managers=data_mapper.map_manager_data()

# for manager in managers:
#     print(f"Manager ID: {manager.id}, Name: {manager.first_name} {manager.last_name}, Team Name: {manager.team_name}")        
manager_dict = {
    manager.id: manager
    for manager in managers
}

# print(manager_dict.keys())

manager_ids=manager_dict.keys()
gameweek=[1,2,3,4,5,6,7,8,9,10]

players=data_mapper.map_player_data()

players_dict = {
    player.id: player
    for player in players
}
# # print(players[0].id)

# # pl_gameweek_history=data_mapper.map_player_gameweek_data(players[0]["player_id"])

# # players[0]["gameweeks"]=pl_gameweek_history

for player in players:
    pl_gameweek_history=data_mapper.map_player_gameweek_data(player.id)

    player.gameweeks=pl_gameweek_history


for manager_id in manager_ids:
    for gw in gameweek:
        playerPick_history=data_mapper.map_playerPick_history(manager_id,gw,players_dict)
        print(playerPick_history)
                

# player_id=69432

# manager_history=data_mapper.map_manager_gameweek_history(player_id)

# for m in manager_history:
#     print(m.bank_value)


# x=players[0].gameweeks[0].points

# print(x)

# url="https://fantasy.premierleague.com/api/element-summary/1/"

# response=requests.get(url)

# response.raise_for_status()

# data=response.json()

# d=data["history"]

# for dx in d:
#     print(dx["element"])
