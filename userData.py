API_KEY = 'calssified'
dataFile = 'data.pkl'
gameFile = 'games.txt'

SUMMONER_ONE_NAME = None
SUMMONER_TWO_NAME = None

SUMMONER_ONE_TAG = None
SUMMONER_TWO_TAG = None


def setSummonerNames():
    global SUMMONER_ONE_NAME, SUMMONER_TWO_NAME, SUMMONER_ONE_TAG, SUMMONER_TWO_TAG
    name_input_1 = input("Enter first summoner name with tag, example name#tag: ")

    # Condition made only for the testing convenience
    if name_input_1 == 'default':
        SUMMONER_ONE_NAME = 'crunchy jelly'
        SUMMONER_ONE_TAG = "Eune"
        SUMMONER_TWO_NAME = 'Dejwμ'
        SUMMONER_TWO_TAG = 'Eune'
        return

    name_input_2 = input("Enter second summoner name with tag, example name#tag: ")

    while len(name_input_1) == 0:
        name_input_1 = input("Name input cannot be blank, enter name again example name#tag: ")

    while len(name_input_2) == 0:
        name_input_2 = input("Name input cannot be blank, enter name again example name#tag: ")

    SUMMONER_ONE_NAME, SUMMONER_ONE_TAG = name_input_1.split('#')
    SUMMONER_TWO_NAME, SUMMONER_TWO_TAG = name_input_2.split('#')
