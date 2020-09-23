import json
import pandas as pd

def player_exist(name):
    """Check if a save exists for player(name)

    Args:
        name (str): The name of the player

    Returns:
        bool: True if player exists, False if player does not.
    """
    try:
        with open(f"saves/{name}.json", 'r'):
            pass
    except FileNotFoundError:
        return False
    else:
        return True


def serialize(coords):
    try:
        with open('saves/test.json', 'r') as f:
            player = json.load(f)
        with open("saves/test.json", "w") as test:
            json.dump(, test)
    except Exception as e:
        print(e)


def deserialize(name):
    try:
        with open(f'saves/{name}.json', 'r') as f:
            player = json.load(f)
            print(player["boards"]["level_one"])
            player["boards"]["level_one"]['3'] = ["c3,c4"]
            print(player["boards"]["level_one"])
    except Exception as e:
        print(e)


def build_playing_field():
    arr = []
    for x in range(10):
        row = []
        for y in range(10):
            row.append("-")
        arr.append(row)

    playing_field = pd.DataFrame(
                      data=arr,
                      index=[
                          '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'
                          ],
                      columns=[
                          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'
                          ])
    return playing_field


test = build_playing_field()
serialize(test)