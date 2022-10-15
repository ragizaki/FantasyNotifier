import requests
from bs4 import BeautifulSoup as bsoup
from datetime import datetime
from players import get_players_from_league

myteam_id = 602008841651027968
league_id = 851541694313775104
injuries_url = "https://www.nfl.com/injuries/"

my_players = [
    f' {player} ' for player in get_players_from_league(myteam_id, league_id)
]

html = requests.get(injuries_url).content
soup = bsoup(html, 'html.parser')
tags = soup.find_all('a', string = my_players)

day = datetime.today().weekday()

# send alert on Monday, Thursday or Sunday (NFL game days)
if day == 0 or day == 3 or day == 6:
    # email
    pass