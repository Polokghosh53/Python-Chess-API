# importing the chessdotcom api with its content for leaderboard, player statistics and player archives of games played
from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint # it is opinionated code formatter used here for json
import requests # fetching the json file from the link

# printing the data received into proper format
printer = pprint.PrettyPrinter()

# fetching the details of Rank, Username and Score of the player
def print_leaderboards():
    data = get_leaderboards().json
    categories = data['leaderboards']
    daily = categories['daily']
    for index in daily:
        print(f" Rank = {index['rank']} | Username = {index['username']} | Score = {index['score']}")

# fetching the details of the Current, Best and Record ratings of the user in the present categories
def get_player_rating(username):
    data = get_player_stats(username).json
    categories = ['chess_blitz','chess_bullet','chess_daily','chess_rapid']
    for category in categories:
        print(f"\nCurrent rating for {category} = {data['stats'][category]['last']['rating']}")
        print(f"Best rating for {category} = {data['stats'][category]['best']['rating']}")
        printer.pprint(f"Record for {category} = {data['stats'][category]['record']}")

# fetching the most recent game of the player
def get_most_recent_game(username):
    data = get_player_game_archives(username).json
    url = data['archives'][-1]
    games = requests.get(url).json()
    game = games['games'][-1]
    printer.pprint(game)

#return the data of the player
print_leaderboards()
get_player_rating('username in chess.com')
get_most_recent_game('username in chess.com')
