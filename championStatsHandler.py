# champion data: number_of_games, wins, kills, deaths, assists, highest dmg, highest shield, most healed, most tanked
# duo data: number_of_games, wins
from fileHandler import loadChampionData

champions_info = loadChampionData()


class ChampionStats:
    number_of_games = 0
    wins = 0

    def __init__(self, name, win, kills, deaths, assists, dmg, shield, heal, tank):
        self.name = name
        increaseGames(self, win)
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.dmg = dmg
        self.shield = shield
        self.heal = heal
        self.tank = tank

    def equals(self, name):
        if self.name == name:
            return True
        else:
            return False

    def update(self, championStats):
        self.number_of_games += 1
        self.wins += championStats.wins
        self.kills += championStats.kills
        self.deaths += championStats.deaths
        self.assists += championStats.assists
        if self.dmg < championStats.dmg:
            self.dmg = championStats.dmg
        if self.shield < championStats.shield:
            self.shield = championStats.shield
        if self.heal < championStats.heal:
            self.heal = championStats.heal
        if self.tank < championStats.tank:
            self.tank = championStats.tank


def addChampion(summoner_data, championsStats: ChampionStats):
    does_exist = False
    for stats in summoner_data:
        if stats.equals(championsStats.name):
            stats.update(championsStats)
            does_exist = True
    if not does_exist:
        summoner_data.append(championsStats)


class DuoStats:
    number_of_games = 0
    wins = 0

    def __init__(self, name_s1, name_s2, win):
        increaseGames(self, win)
        self.name_s1 = name_s1
        self.name_s2 = name_s2

    def equals(self, name_s1, name_s2):
        if self.name_s1 == name_s1 and self.name_s2 == name_s2:
            return True
        else:
            return False


def addDuo(duo_data, champion_name_s1, champion_name_s2, win):
    does_exist = False
    for stats in duo_data:
        if stats.equals(champion_name_s1, champion_name_s2):
            increaseGames(stats, win)
            does_exist = True
    if not does_exist:
        duo_data.append(DuoStats(champion_name_s1, champion_name_s2, win))


def increaseGames(championStats, didWin):
    if didWin:
        championStats.wins += 1
    championStats.number_of_games += 1
