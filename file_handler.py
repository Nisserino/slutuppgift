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


def init_player(name):
    try:
        with open(f"saves/{name}.json", "w") as f:
            base_json = {
                        "boards": {
                        },
                        "stats": {
                            "wins": {
                                },
                            "losses": {
                                }
                            }
                        }
            json.dump(base_json, f)
    except Exception as e:
        print(f"Error: {e}")
        raise


def serialize_board(coords, name, board_name):
    try:
        with open(f"saves/{name}.json", "r") as f:
            player = json.load(f)
            player["boards"][board_name] = coords
        with open(f"saves/{name}.json", "w") as test:
            json.dump(player, test)
    except Exception as e:
        print(e)
        raise


def deserialize(board):
    try:
        with open("saves/gustav.json", "r") as f:
            player = json.load(f)
            board_pos = player["boards"]["level_one"]
            for boat, i in enumerate(board_pos):
                for boats in board_pos[i]:
                    board_from_file(board, board_pos[i], i)
    except Exception as e:
        print(e)
        raise


def board_from_file(board, coord_list, ship_num):
    for coord in coord_list:
        board.loc[coord[0], coord[1]] = ship_num


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


ship_coords = {
                4: [['5', 'b'], ['5', 'c'], ['5', 'd'], ['5', 'e']],
                3: [['1', 'j'], ['2', 'j'], ['3', 'j'], ['9', 'a'],
                    ['9', 'b'], ['9', 'c']],
                2: [['1', 'c'], ['2', 'c'], ['3', 'g'], ['3', 'h'],
                    ['7', 'f'], ['8', 'f']],
                1: [['1', 'a'], ['6', 'i'], ['9', 'g'], ['9', 'i']]
                }


# test = build_playing_field()
# serialize_board(ship_coords, "gunhild", "other_board")
