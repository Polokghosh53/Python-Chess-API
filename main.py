from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()

def print_leaderboards():
    data = get_leaderboards().json
    categories = data['leaderboards']
    daily = categories['daily']
    for index in daily:
        print(f" Rank = {index['rank']} | Username = {index['username']} | Score = {index['score']}")


def get_player_rating(username):
    data = get_player_stats(username).json
    categories = ['chess_blitz','chess_bullet','chess_daily','chess_rapid']
    for category in categories:
        print(f"\nCurrent rating for {category} = {data['stats'][category]['last']['rating']}")
        print(f"Best rating for {category} = {data['stats'][category]['best']['rating']}")
        printer.pprint(f"Record for {category} = {data['stats'][category]['record']}")

def get_most_recent_game(username):
    data = get_player_game_archives(username).json
    url = data['archives'][-1]
    games = requests.get(url).json()
    game = games['games'][-1]
    printer.pprint(game)

print_leaderboards()
get_player_rating('cschess')
get_most_recent_game('cschess')
