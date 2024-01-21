import userData
from dataHandler import uniqueChampions, sharedChampions, highestWinRate, classDistribution
from championStatsHandler import ChampionStats, addChampion, addDuo, champions_info
from connectionHandler import getGames, getGameData
from dataVisualisation import createGraphs, createTableUniqueChampions, createHTML, createTableSharedChampions, \
    createWinningComps
from fileHandler import addGame, load_from_pickle, save_to_pickle, calculateNumberOfGames

userData.setSummonerNames()

summoner_one_data, summoner_two_data, duo_data = load_from_pickle(userData.dataFile)
games_info = getGames(userData.API_KEY, userData.SUMMONER_ONE_NAME, userData.SUMMONER_ONE_TAG)
summoners_rift = 11
arena = 30
for game in games_info:
    match_data = getGameData(userData.API_KEY, game)
    if match_data['info']['mapId'] == summoners_rift:
        if addGame(userData.gameFile, game):

            champion_data_s1 = None
            champion_data_s2 = None
            win = None

            for i in match_data['info']['participants']:

                if i['summonerName'] == userData.SUMMONER_ONE_NAME:

                    print(i['summonerName'], i['championName'])
                    champion_data_s1 = ChampionStats(i['championName'], i["win"],
                                                     i['kills'], i['deaths'], i['assists'],
                                                     i['totalDamageDealtToChampions'],
                                                     i['totalDamageShieldedOnTeammates'],
                                                     i['totalHeal'], i['totalDamageTaken'])

                    addChampion(summoner_one_data, champion_data_s1)

                    print("----")
                elif i['summonerName'] == userData.SUMMONER_TWO_NAME:
                    print(i['summonerName'], i['championName'])

                    champion_data_s2 = ChampionStats(i['championName'], i["win"],
                                                     i['kills'], i['deaths'], i['assists'],
                                                     i['totalDamageDealtToChampions'],
                                                     i['totalDamageShieldedOnTeammates'],
                                                     i['totalHeal'], i['totalDamageTaken'])

                    addChampion(summoner_two_data, champion_data_s2)
                    win = i["win"]

            print("#####")

            if champion_data_s1 is not None and champion_data_s2 is not None:
                addDuo(duo_data, champion_data_s1.name, champion_data_s2.name, win)

save_to_pickle(userData.dataFile, summoner_one_data, summoner_two_data, duo_data)

top_champs_s1 = highestWinRate(summoner_one_data)
top_champs_s2 = highestWinRate(summoner_two_data)

unique_champs_s1 = uniqueChampions(summoner_one_data)
unique_champs_s2 = uniqueChampions(summoner_two_data)

class_distribution_s1 = classDistribution(summoner_one_data, champions_info["data"])
class_distribution_s2 = classDistribution(summoner_two_data, champions_info["data"])

shared_champs = sharedChampions(summoner_one_data, summoner_two_data)

createGraphs(userData.SUMMONER_ONE_NAME, userData.SUMMONER_TWO_NAME,
             class_distribution_s1, class_distribution_s2,
             top_champs_s1, top_champs_s2
             )
unique_champions_table = createTableUniqueChampions(userData.SUMMONER_ONE_NAME, userData.SUMMONER_TWO_NAME,
                                                    unique_champs_s1, unique_champs_s2)

shared_champions_table = createTableSharedChampions(shared_champs)

winning_comps_table = createWinningComps(duo_data)

number_of_games = calculateNumberOfGames(userData.gameFile)

createHTML(userData.SUMMONER_ONE_NAME, userData.SUMMONER_TWO_NAME, unique_champions_table, shared_champions_table,
           winning_comps_table, number_of_games)
