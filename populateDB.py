# Run this file ONCE, to populate the data.json file with a list of active
#   NFL players. This is later used to query the players on a given league
#   and team in players.py

import requests
import json

players_endpoint = 'https://api.sleeper.app/v1/players/nfl'

players_json = requests.get(players_endpoint).json()

with open("data.json", "w") as file:
    json.dump(players_json, file)