import requests
import json
from typing import List

base_url = 'https://api.sleeper.app/v1'

# returns players on team with myteam_id from league with league_id
def get_players_from_league(myteam_id: str, league_id: str) -> List[str]:
    league_endpoint = f'{base_url}/league/{league_id}/rosters'

    teams = requests.get(league_endpoint).json()
    my_team = next(team for team in teams if team["owner_id"] == str(myteam_id))

    # removes the defense from the ID's, as they can never be injured
    # and thus are not relevant to this project
    player_ids = my_team["starters"][:-1]

    with open("data.json") as file:
        players = json.load(file)

    player_names = [players[id]["full_name"] for id in player_ids]

    return player_names