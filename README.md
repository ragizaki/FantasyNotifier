# Sleeper Fantasy Football Notifier
Being in a fantasy football league with my friends through the Sleeper app, I've had the problem of having players get injured near games. I will usually miss these updates and leave the players in my starting lineup, thus lowering my points. I built a scraper that sends an SMS before games to notify a fantasy user of any injured players. Note that this only works for fantasy leagues in Sleeper, and requires the league ID and team ID (which are easily accessible through the app).

This app uses the [Sleeper API](https://docs.sleeper.app/) endpoints to fetch a player's team from their league, as well as populating the `data.json` file with a list of NFL players (this is only done once, as the request is large).

To use the project, follow these commmands:
```
git clone ...
cd fantasy-football-notifier
python3 main.py <LEAGUE_ID> <TEAM_ID> <EMAIL_ADDRESS>
```

Running this will send a list of players to the given email address (must be a Gmail account). This process can be automated externally from CRON or Windows Schedule manager, etc.


## TODO
- Currently, the script has no way of discerning on which days an injured player is scheduled for. Thus, I'm planning to scrape the players' game dates and send messages on the condition that they have an upcoming game.
- The user running the script is currently responsible for automating the script. It would be a better user experience if the automation functionality was out of the box from the script.
