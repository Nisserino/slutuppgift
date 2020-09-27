import file_handler as fh
import funcs as f


class Game():
    def __init__(self, board_1, board_2):
        display_1 = fh.build_playing_field()
        display_2 = fh.build_playing_field()
        self.players = [board_1, board_2]
        self.display_boards = [display_1, display_2]
        self.turn = 1

    def shoot_(self, prompt, arg):
        coord = f.coord_format(arg)
        if "1" in prompt:
            self.shoot(0, coord)
        else:
            self.shoot(1, coord)

    def shoot(self, player_num, coord):
        if self.hit(player_num, coord):
            if self.sunk(coord, self.players[player_num]):
                self.players[player_num].loc[coord[0], coord[1]] = "X"
                print("You sunk the ship!")
            else:
                self.players[player_num].loc[coord[0], coord[1]] = "x"
                print("Ship is hit, but still afloat!")
        else:
            print("Miss!")
            self.players[player_num].loc[coord[0], coord[1]] = "o"
            self.turn_over()
        print(
            f"-- player 1 --\n{self.players[0]}\n"
            f"-- player 2 --\n{self.players[1]}"
            )

    def hit(self, player_num, coord):
        if self.players[player_num].loc[coord[0], coord[1]].isdigit():
            return True
        else:
            return False

    def sunk(self, hit_coord, board):
        if board.loc[hit_coord[0], hit_coord[1]] == "1":
            return True
        elif board.loc[hit_coord[0], hit_coord[1]] == "2":
            return self.func_1([hit_coord], board, 2)
        elif board.loc[hit_coord[0], hit_coord[1]] == "3":
            return self.func_1([hit_coord], board, 3)
        elif board.loc[hit_coord[0], hit_coord[1]] == "4":
            return self.func_1([hit_coord], board, 4)

    def func_1(self, hit_coord, board, ship_size):
        ship_coords = []
        for coord in hit_coord:
            ship_coords.append(coord)
        if len(ship_coords) < ship_size:
            boat_coords = []
            for coord in ship_coords:
                boat_coords.append(self.func_2(coord, board))
            for lists in boat_coords:
                for coord in lists:
                    if coord not in ship_coords:
                        ship_coords.append(coord)
        if len(ship_coords) != ship_size:
            self.func_1(ship_coords, board, ship_size)
        else:
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

    def func_2(self, coord, board):
        hits = []
        check = ["2", "3", "4", "x"]
        lindex, lolumns = f.list_ind_col(board)
        i_start = lindex.index(coord[0])
        c_start = lolumns.index(coord[1])
        if board.loc[lindex[i_start - 1], lolumns[c_start]] in check:
            hits.append([lindex[i_start - 1], lolumns[c_start]])
        if board.loc[lindex[i_start], lolumns[c_start - 1]] in check:
            hits.append([lindex[i_start], lolumns[c_start - 1]])
        if board.loc[lindex[i_start + 1], lolumns[c_start]] in check:
            hits.append([lindex[i_start + 1], lolumns[c_start]])
        if board.loc[lindex[i_start], lolumns[c_start + 1]] in check:
            hits.append([lindex[i_start], lolumns[c_start + 1]])
        return hits

    def turn_over(self):
        self.turn += 1


# board_1 = fh.deserialize("gunhild", "feltet")
# board_2 = fh.deserialize("pc", "pog")
# test_game = Game(board_1, board_2)
# test_game.shoot(0, ["1", "b"])
