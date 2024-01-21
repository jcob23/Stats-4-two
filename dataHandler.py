def uniqueChampions(data):
    return set([championStats.name for championStats in data])


def sharedChampions(data_s1, data_s2):
    return set([championStats.name for championStats in data_s1]) & set(
        [championStats.name for championStats in data_s2])


def highestWinRate(data):
    sorted_data = sorted(data, key=lambda x: x.wins, reverse=True)
    top_champs = []
    for championStats in sorted_data:
        win_rate = championStats.wins / championStats.number_of_games * 100
        data = [championStats.name, win_rate, championStats.number_of_games]
        top_champs.append(data)
        if len(top_champs) == 4:
            return top_champs


def classDistribution(summoner_data, championsInfo):
    tags = {"Tank": 0, "Mage": 0, "Assassin": 0, "Fighter": 0, "Marksman": 0, "Support": 0}
    champions = []
    for championStats in summoner_data:
        for i in range(0, championStats.number_of_games):
            champions.append(championStats.name)

    for champion in champions:
        tag = championsInfo[champion]['tags'][0]
        tags[tag] += 1

    return tags
