import file_handler as fh
import funcs as f
import random


class Game():
    """Holds the 'game' contained, keeping check of who's playing
    What the turn-counter is, when someone has won, and if you're playing
    vs a human or pc
    also contains all actions you can make, such as shoot, or see hp
    args:
    board1 : [pandas.Dataframe] : player1s board
    board2 : [pandas.Dataframe] : player2s board (unless pve)
    pvp : [bool] : True if pvp, False if pve
    """
    def __init__(self, board_1, board_2, pvp):
        display_1 = f.build_playing_field()
        display_2 = f.build_playing_field()
        self.players = [board_1, board_2]
        self.display_boards = [display_1, display_2]
        self.turn = 1
        self.pvp = pvp
        self.hp = [20, 20]
        self.game_over = False

    # See who shot
    def shoot_who(self, prompt, arg):
        coord = f.coord_format(arg)
        if "1" in prompt:
            self.check_shot(1, coord)  # Shoot other player
        else:
            self.check_shot(0, coord)  # -//-

    # Make sure hit coords are correct, and that it wasn't shot already
    def check_shot(self, player, coord):
        try:
            target = self.players[player].loc[coord[0], coord[1]]
            if target == "o" or target == "x" or target == "X":
                print("You have already shot there, shoot elsewhere!")
            else:
                self.check_hit(player, coord)
        except Exception as e:  # KeyError and Index error
            print(
                f"Error: {e}\n"
                "You probably wrote the coords badly\nTry again."
                )

    # Check what kind of hit it was
    def check_hit(self, player, coord):
        if self.hit(player, coord):  # Hit or miss
            self.check_afloat(player, coord)  # Hit or sink
        else:
            print("Miss!")
            self.players[player].loc[coord[0], coord[1]] = "o"
            self.display_boards[player].loc[coord[0], coord[1]] = "o"
            self.turn_over()
        self.show_boards()

    # Check if the shot was a hit or a miss
    def hit(self, player_num, coord):
        coord = self.players[player_num].loc[coord[0], coord[1]]
        if coord.isdigit():
            self.hp[player_num] -= 1
            return True
        else:
            return False

    # Start of sunk-check, if check_boat returns True, it is sunk
    def check_afloat(self, player, coord):
        if self.check_boat(coord, self.players[player]):
            self.players[player].loc[coord[0], coord[1]] = "X"
            self.display_boards[player].loc[coord[0], coord[1]] = "X"
            self.win_check(player)
            print("You sunk the ship!")
        else:
            self.players[player].loc[coord[0], coord[1]] = "x"
            self.display_boards[player].loc[coord[0], coord[1]] = "x"
            print("Ship is hit, but still afloat!")

    # Get shipsize to help the next func
    def check_boat(self, hit_coord, board):
        # Get shipsize, if ship is a 1, it has sunk (return True)
        if board.loc[hit_coord[0], hit_coord[1]] == "1":
            return True
        elif board.loc[hit_coord[0], hit_coord[1]] == "2":
            return self.find_boat([hit_coord], board, 2)
        elif board.loc[hit_coord[0], hit_coord[1]] == "3":
            return self.find_boat([hit_coord], board, 3)
        elif board.loc[hit_coord[0], hit_coord[1]] == "4":
            return self.find_boat([hit_coord], board, 4)

    # Send hit coord to find adjacant, get adjacant ship pieces back
    # Check all ship pieces untill their len == shipsize, check if boat is dead
    def find_boat(self, hit_coord, board, ship_size):
        ship_coords = []
        for coord in hit_coord:
            ship_coords.append(coord)
        while len(ship_coords) < ship_size:
            boat_coords = []
            for coord in ship_coords:
                boat_coords.append(self.find_adjacant(coord, board))
            for lists in boat_coords:
                for coord in lists:
                    if (coord not in ship_coords):
                        ship_coords.append(coord)
        return self.boat_dead(ship_coords, board)

    # Find all adjacant pieces of boat from a coord.
    def find_adjacant(self, coord, board):
        hits = []
        check = ["2", "3", "4", "x"]
        lindex, lolumns = f.list_ind_col(board)  # [index], [columns] in lists
        i_start = lindex.index(coord[0])  # Start of index from coord
        c_start = lolumns.index(coord[1])  # Start of columns from coord
        try:
            if board.loc[lindex[abs(i_start - 1)], lolumns[c_start]] in check:
                hits.append([lindex[abs(i_start - 1)], lolumns[c_start]])
            if board.loc[lindex[i_start], lolumns[abs(c_start - 1)]] in check:
                hits.append([lindex[i_start], lolumns[abs(c_start - 1)]])
            if board.loc[lindex[i_start + 1], lolumns[c_start]] in check:
                hits.append([lindex[i_start + 1], lolumns[c_start]])
            if board.loc[lindex[i_start], lolumns[c_start + 1]] in check:
                hits.append([lindex[i_start], lolumns[c_start + 1]])
        except IndexError:
            pass
        return hits

    # Check if boat is floating or has sunk, takes a list of whole boats coords
    def boat_dead(self, ship_coords, board):
        sunk = []
        for coord in ship_coords:
            if board.loc[coord[0], coord[1]].isdigit():
                sunk.append(1)
            else:
                sunk.append(0)
        if sunk.count(1) == 1:
            return True
        else:
            return False

    # Show the playing fields without the boats visible.
    def show_boards(self):
        print(
            f"-- Player 1 -- \n{self.display_boards[0]}\n"
            f"-- Player 2 -- \n{self.display_boards[1]}"
        )

    def turn_over(self):
        self.turn += 1

    def win_check(self, player_num):
        if self.hp[player_num] == 0:
            self.game_over = True


class Bot_player:
    def __init__(self):
        self.start()  # Picks a random board from user pc
        self.shootable_coords()  # initializes list of attackable coords
        self.last_hit = str  # Store last hit, unless ship sunk

    # Helper func to initialize bot obj.
    def start(self):
        name = "pc"
        boards = fh.player_boards(name)
        board = boards[random.randint(0, len(boards) - 1)]
        self.board = fh.deserialize(name, board)

    # Make a list of all allowed coordinates (100)
    def shootable_coords(self):
        df = f.build_playing_field()
        lolumns, lindex = f.list_ind_col(df)
        self.attackable = []
        for i in lindex:
            for c in lolumns:
                coord = [i, c]
                if coord not in self.attackable:
                    self.attackable.append(coord)

    # Shoot at a random coord that is attackable,
    # remove coord from attackable list
    def fire(self):
        move = random.randint(0, len(self.attackable) - 1)
        choice = self.attackable[move]
        del self.attackable[move]
        return choice

    # Extra piece for later
    def smart_shot():
        pass
