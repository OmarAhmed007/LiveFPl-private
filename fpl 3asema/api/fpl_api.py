import requests

class APIManager:
    def __init__(self):
        self.base_url = "https://fantasy.premierleague.com/api/"

    def get_manager_data(self,manager_id):
        url=f"{self.base_url}entry/{manager_id}/"
        try:
            response=requests.get(url)
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"Error fetching manager data: {e}")
            return None

        return response.json()
    def get_player_data(self):
        url=f"{self.base_url}/bootstrap-static/"
        try:
            response=requests.get(url)
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"Error fetching player data: {e}")
            return None

        data=response.json()

        players=data["elements"]

        return players    


    def get_player_gameweek_data(self,player_id):
       
        url=f"{self.base_url}/element-summary/{player_id}"
        try:
            response=requests.get(url)
            response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching player gameweek data: {e}")
            return None

        data=response.json()

        return data["history"]


    def get_manager_gameweek_history(self,manager_id):
        url=f"{self.base_url}/entry/{manager_id}/history"
        try:
            response=requests.get(url)
            response.raise_for_status()
                    
        except requests.exceptions.RequestException as e:
                print(f"Error fetching player gameweek data: {e}")
                return None

        data=response.json()

        return data


    def get_playerPick_history(self,manager_id,gameweek):
          url=f"{self.base_url}/entry/{manager_id}/event/{gameweek}/picks/"

          try:
              response=requests.get(url)
              response.raise_for_status()
                      
          except requests.exceptions.RequestException as e:
                  print(f"Error fetching player gameweek data: {e}")
                  return None
          data=response.json()
          return data
        
    





                        
            

        


    

