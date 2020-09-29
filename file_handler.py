import json
import csv
import funcs


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


def deserialize(name, board_name):
    board = funcs.build_playing_field()
    try:
        with open(f"saves/{name}.json", "r") as f:
            player = json.load(f)
            board_pos = player["boards"][board_name]
            for boat, i in enumerate(board_pos):
                for boats in board_pos[i]:
                    board_from_file(board, board_pos[i], i)
        return board
    except Exception as e:
        print(e)
        raise


def player_boards(name):
    try:
        boards = []
        with open(f"saves/{name}.json", "r") as f:
            player = json.load(f)
            for board in player["boards"]:
                boards.append(board)
        return boards
    except Exception as e:
        print(f"Error: {e}")


def board_from_file(board, coord_list, ship_num):
    for coord in coord_list:
        board.loc[coord[0], coord[1]] = ship_num
    return board


def logg_game(winner, loser, turns):
    with open("saves/logg.csv", "a", newline='') as f:
        csv.writer(f).writerow((winner, loser, turns))
        print("done")
