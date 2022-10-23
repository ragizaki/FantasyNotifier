import requests
import smtplib
import os
import sys
from datetime import datetime
from bs4 import BeautifulSoup as bsoup
from players import get_players_from_league

SENDER = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
injuries_url = "https://www.nfl.com/injuries/"

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("USAGE: python3 main.py <SLEEPER_LEAGUE_ID> <SLEEPER_TEAM_ID> <EMAIL_ADDRESS>")
    else:
        league_id = sys.argv[1]
        team_id = sys.argv[2]
        receiver = sys.argv[3]

        players = [
             f' {player} ' for player in get_players_from_league(team_id, league_id)
        ]

        html = requests.get(injuries_url).content
        soup = bsoup(html, 'html.parser')
        tags = soup.find_all('a', string = players)
        formattedPlayers = ','.join(tags)

        now = datetime.now()
        format = "%m/%d/%Y"
        today = now.strftime(format)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(SENDER, EMAIL_PASSWORD)

            subject = f'Injured Fantasy Players for {today}'
            body = f'The following players are injured: {players}'

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(SENDER, receiver, msg)
    