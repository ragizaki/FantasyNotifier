import requests
import smtplib
import os
from datetime import datetime
from bs4 import BeautifulSoup as bsoup
from players import get_players_from_league

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


myteam_id = 602008841651027968
league_id = 851541694313775104
injuries_url = "https://www.nfl.com/injuries/"

my_players = [
    f' {player} ' for player in get_players_from_league(myteam_id, league_id)
]

html = requests.get(injuries_url).content
soup = bsoup(html, 'html.parser')
tags = soup.find_all('a', string = my_players)
players = ','.join(tags)

now = datetime.now()
format = "%m/%d/%Y"
today = now.strftime(format)

# sending email with SMTP, this process is automated externally with cron
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = f'Injured Fantasy Players for {today}'
    body = f'The following players are injured: {players}'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)