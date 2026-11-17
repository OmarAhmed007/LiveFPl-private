import time
import requests


class APIManager:
    RETRY_STATUS = (429, 500, 502, 503, 504)

    def __init__(self, timeout=10, retries=3, delay=0.05):
        self.base_url = "https://fantasy.premierleague.com/api/"
        self.session = requests.Session()
        self.timeout = timeout
        self.retries = retries
        self.delay = delay  # small pause between calls to avoid rate limits

    def _get(self, path):
        """GET a path under base_url and return parsed JSON.

        Returns None if the resource doesn't exist (404) or if the request
        still fails after all retries.
        """
        url = f"{self.base_url}{path}"

        for attempt in range(self.retries):
            try:
                response = self.session.get(url, timeout=self.timeout)

                if response.status_code == 404:
                    return None  # legitimately missing, don't retry

                if response.status_code in self.RETRY_STATUS:
                    print(f"{response.status_code} for {url}, retrying (attempt {attempt + 1})")
                    time.sleep(2 ** attempt)
                    continue

                response.raise_for_status()
                time.sleep(self.delay)
                return response.json()

            except (requests.exceptions.RequestException, ValueError) as e:
                # ValueError covers invalid JSON in the response body
                print(f"Attempt {attempt + 1} failed for {url}: {e}")
                time.sleep(2 ** attempt)

        print(f"Giving up on {url} after {self.retries} attempts")
        return None

    def get_manager_data(self, manager_id):
        return self._get(f"entry/{manager_id}/")

    def get_player_data(self):
        data = self._get("bootstrap-static/")
        if data is None:
            return None
        return data["elements"]

    def get_player_gameweek_data(self, player_id):
        data = self._get(f"element-summary/{player_id}/")
        if data is None:
            return None
        return data["history"]

    def get_manager_gameweek_history(self, manager_id):
        return self._get(f"entry/{manager_id}/history/")

    def get_playerPick_history(self, manager_id, gameweek):
        return self._get(f"entry/{manager_id}/event/{gameweek}/picks/")
