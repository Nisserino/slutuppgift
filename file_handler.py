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
    """Create a player with user given name
    Builds the skeleton for the json file so the other funcs
    Will work properly

    Args:
        name (str): The name of the player
    """
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
    """Save a board to given users player-file

    Args:
        coords (dict): dict with all coords as value, shipsize as key
        name (str): Name of the player to whom the bord belongs
        board_name (str): The name you want to save your board as
    """
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
    """Deserialize chosen players chosen bord
    return a board populated by players ships

    Args:
        name (str): Name of the player
        board_name (str): Name of the board

    Returns:
        pd.dataframe: Board with players ships
    """
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
    """Get all boards chosen player has made

    Args:
        name (str): Player name

    Returns:
        list: List of boards player has made
    """
    try:
        boards = []
        with open(f"saves/{name}.json", "r") as f:
            player = json.load(f)
            for board in player["boards"]:
                boards.append(board)
        return boards
    except Exception as e:
        print(f"Error: {e}")


# Helper func for deserialize
def board_from_file(board, coord_list, ship_num):
    for coord in coord_list:
        board.loc[coord[0], coord[1]] = ship_num
    return board


def logg_game(winner, loser, turns):
    with open("saves/logg.csv", "a", newline="") as f:
        csv.writer(f).writerow((winner, loser, turns))
        print("done")


def show_logg():
    with open("saves/logg.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for line in reader:
            print(line)
