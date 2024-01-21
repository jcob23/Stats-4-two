import json
import pickle


def addGame(file_name, game_id):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            if game_id not in text:
                with open(file_name, 'a') as file_save:
                    if game_id == "status":
                        return False
                    file_save.write(game_id + '\n')
                    print(f'Dodano "{game_id}" do pliku.')
                    return True
            else:
                print(f'String "{game_id}" już istnieje w pliku.')
                return False

    except FileNotFoundError:
        with open(file_name, 'w') as new_file:
            new_file.write(game_id + '\n')
            print(f'Nowy plik stworzony, dodano "{game_id}" do pliku.')
            return True


def save_to_pickle(filename, *arrays):
    with open(filename, 'wb') as file:
        pickle.dump(arrays, file)


def load_from_pickle(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except:
        return [], [], []


def loadChampionData():
    with open("champion.json", 'r') as file:
        return json.load(file)


def calculateNumberOfGames(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        line_count = sum(1 for line in file)
        return line_count
