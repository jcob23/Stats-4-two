import requests


def getGames(api_key, name_s1, tag):
    puuid = get_puuid_by_riot_id(name_s1, tag, api_key)
    link = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/"
    api_url_games = link + puuid + "/ids?start=0&count=50&api_key=" + api_key
    return requests.get(api_url_games).json()


def get_puuid_by_riot_id(game_name, tag_line, api_key):
    api_url = f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    headers = {"X-Riot-Token": api_key}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()['puuid']
    else:
        return response


def getGameData(api_key, game):
    api_url_last_game_info = "https://europe.api.riotgames.com/lol/match/v5/matches/" + game
    api_url_last_game_info = api_url_last_game_info + '?api_key=' + api_key
    return requests.get(api_url_last_game_info).json()
