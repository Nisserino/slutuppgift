import pandas as pd
import file_handler as fh


def list_ind_col(board):
    lindex = [i for i in board.index]
    lolumns = [i for i in board.columns]
    return lindex, lolumns


def find_coords(board):
    boats = [1, 2, 3, 4]
    lindex, lolumns = list_ind_col(board)
    boat_coords = []
    to_json = {
        4: [],
        3: [],
        2: [],
        1: []
    }
    for i in lindex:
        for c in lolumns:
            if board.loc[i, c] in boats:
                boat_coords.append([i, c, board.loc[i, c]])
    for coord in boat_coords:
        to_json[coord[2]].append(coord[0:2])
    return to_json


# Reomve boats, in if, check .isdigt() instead
def adjacant_check(coord_list, board):
    lindex, lolumns = list_ind_col(board)
    positions_allowed = True
    boats = [1, 2, 3, 4]
    try:
        for coord in coord_list:
            ind_start = lindex.index(coord[0])
            col_start = lolumns.index(coord[1])
            if board.loc[lindex[ind_start - 1], lolumns[col_start]] in boats:
                positions_allowed = False
            elif board.loc[lindex[ind_start], lolumns[col_start + 1]] in boats:
                positions_allowed = False
            elif board.loc[lindex[ind_start + 1], lolumns[col_start]] in boats:
                positions_allowed = False
            elif board.loc[lindex[ind_start], lolumns[col_start - 1]] in boats:
                positions_allowed = False
    except IndexError:
        pass
    except Exception as e:
        print(f"Error: {e}")
        raise
    return positions_allowed


def board_check(coord_list, board, ship_size):
    """Check if you are allowed to place a boat at coordinate 1 going towards
    coordinate 2 for ship_size steps
    returns a bool True if it's allowed, False if it's not

    Args:
        coord_list (list): List of first and second coordinate for your boat
        board (pd.dataframe): The players board you want to place boats on
        ship_size (int): Size of the boat you want to place

    Returns:
        list: if all coords of boat is allowed, list of coords returned
        bool: if boat has any unallowed coords, False is returned
    """
    lindex, lolumns = list_ind_col(board)
    coord1 = coord_list[0]  # numbers
    coord2 = coord_list[1]  # letter
    positions_allowed = False
    boat = []
    if coord1[0] == coord2[0]:
        positions_allowed = True
        start = lolumns.index(coord1[1])
        for x in range(ship_size):
            if board.loc[coord1[0], lolumns[start + x]] != "-":
                positions_allowed = False
            else:
                boat.append([coord1[0], lolumns[start + x]])
    elif coord1[1] == coord2[1]:
        positions_allowed = True
        start = lindex.index(coord1[0])
        for x in range(ship_size):
            if board.loc[lindex[start + x], coord1[1]] != "-":
                positions_allowed = False
            else:
                boat.append([lindex[start + x], coord1[1]])
    if positions_allowed:
        if adjacant_check(boat, board):
            return boat
        else:
            print("Boat in adjacant tile!")
            return False
    else:
        print("Boat already in tile!")
        return False


def place_boat(coord_list, board, ship_size):
    coords = board_check(coord_list, board, ship_size)
    if coords:
        for coord in coords:
            board.loc[coord[0], coord[1]] = ship_size
    else:
        return False


def place_ships(board):
    ship_4(board)
    for _ in range(2):
        ship_3(board)
    for _ in range(3):
        ship_2(board)
    for _ in range(4):
        ship_1(board)
    print(f"{board}\nThis is your board!")
    return board


def ship_1(board):
    print(board)
    print("\nWhat position would you like to add ship of size 1 to?")
    try:
        coord = coord_format(input_handler())
        if board.loc[coord[0], coord[1]] == "-":
            board.loc[coord[0], coord[1]] = 1
        else:
            print("There is already a ship there.")
            ship_1(board)
    except KeyError:
        print("Couldn't find that in the coordinate system\nTry again.")
        ship_1(board)
    except IndexError:
        print("Index error, you did something wrong")
        ship_1(board)
    except TypeError:
        print("Faulty input\n")
        ship_1(board)


def ship_2(board):
    print(board)
    print("\nWhat position do you want to add a ship of size 2 to?")
    try:
        pos1, pos2 = parse(input_handler())
        coords = coord_format(pos1, pos2)
        if place_boat(coords, board, 2) is False:
            ship_2(board)
    except IndexError:
        print("Index error, you tried to place boat outside of the board")
        ship_2(board)
    except Exception as e:
        print(f"boat 2 err: {e}")


def ship_3(board):
    print(board)
    print("\nWhat position do you want to add a ship of size 3 to?")
    try:
        pos1, pos2 = parse(input_handler())
        coords = coord_format(pos1, pos2)
        if place_boat(coords, board, 3) is False:
            ship_3(board)
    except IndexError:
        print("Index error, you tried to place boat outside of the board")
        ship_3(board)
    except Exception as e:
        print(f"boat 3 err: {e}")


def ship_4(board):
    print(board)
    print("\nWhat position do you want to add a ship of size 4 to?")
    try:
        pos1, pos2 = parse(input_handler())
        coords = coord_format(pos1, pos2)
        if place_boat(coords, board, 4) is False:
            ship_4(board)
    except IndexError:
        print("Index error, you tried to place boat outside of the board")
        ship_4(board)
    except Exception as e:
        print(f"boat 4 err: {e}")
        raise


def make_player(name):
    if fh.player_exist(name) is False:
        fh.init_player(name)
        print(f"Created a player: {name}")
    else:
        print(f"Player: {name} already exists")


def make_board(arg):
    player_name, board_name = parse(arg)
    if fh.player_exist(player_name):
        board = build_playing_field()
        place_ships(board)
        fh.serialize_board(find_coords(board), player_name, board_name)
    else:
        print("Player does not exist, please create you profile first!")


def show_players():
    pass


def show_player_boards(player):
    pass


# For future, if I want playfields bigger than alphabet, len(letter) <= 1
def coord_format(*coords):
    list_coords = []
    try:
        for coord in coords:
            numbers = ''
            letter = ''
            for char in coord:
                if char.isdigit():
                    numbers += char
                else:
                    letter += char
            if len(letter) == 1 and len(numbers) <= 2:
                coord = [numbers, letter]
                list_coords.append(coord)
        if len(list_coords) == 1:
            return list_coords[0]
        else:
            return list_coords
    except TypeError:
        print("No input found")
        raise


def input_handler():
    try:
        usr_in = input("\n: ")
        return usr_in.lower()
    except Exception as e:
        print(f"Error: {e}")


def parse(arg):
    try:
        if "," in arg:
            args = tuple(arg.split(","))
            args = [arg.strip() for arg in args]
            return args
        else:
            return arg.strip().lower()
    except Exception as e:
        print(f"Error: {e}")


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
