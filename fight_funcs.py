import file_handler as fh
import funcs as f


class Game():
    def __init__(self, board_1, board_2):
        display_1 = fh.build_playing_field()
        display_2 = fh.build_playing_field()
        self.players = [board_1, board_2]
        self.display_boards = [display_1, display_2]
        self.turn = 1

    def shoot(self, player_num, coord):
        if self.hit(player_num, coord):
            print("Hit!")
            if self.sunk(coord, self.players[player_num]):
                self.players[player_num].loc[coord[0], coord[1]] = "X"
            else:
                self.players[player_num].loc[coord[0], coord[1]] = "x"
        else:
            print("Miss!")
            self.players[player_num].loc[coord[0], coord[1]] = "o"
            self.turn_over()
        print(self.players[player_num])

    def hit(self, player_num, coord):
        if self.players[player_num].loc[coord[0], coord[1]].isdigit():
            return True
        else:
            return False

    def sunk(self, hit_coord, board):
        if board.loc[hit_coord[0], hit_coord[1]] == "1":
            return True
        elif board.loc[hit_coord[0], hit_coord[1]] == "2":
            pass
        elif board.loc[hit_coord[0], hit_coord[1]] == "3":
            pass
        elif board.loc[hit_coord[0], hit_coord[1]] == "4":
            self.check_adj(hit_coord, board, 4)

    # unfinished, rework coming up!
    def check_adj(self, hit_coord, board, ship_size):
        check = ["2", "3", "4", "x"]
        lindex, lolumns = f.list_ind_col(board)
        ship = [hit_coord]
        while len(ship) < ship_size:
            i_start = lindex.index(ship[-1][0])
            c_start = lolumns.index(ship[-1][1])
            to_ship = []
            if board.loc[lindex[i_start - 1], lolumns[c_start]] in check:
                to_ship = [lindex[i_start - 1], lolumns[c_start]]
            elif board.loc[lindex[i_start], lolumns[c_start - 1]] in check:
                to_ship = [lindex[i_start], lolumns[c_start - 1]]
            elif board.loc[lindex[i_start + 1], lolumns[c_start]] in check:
                to_ship = [lindex[i_start + 1], lolumns[c_start]]
            elif board.loc[lindex[i_start], lolumns[c_start + 1]] in check:
                to_ship = [lindex[i_start], lolumns[c_start + 1]]
            if to_ship not in ship:
                ship.append(to_ship)

    def turn_over(self):
        self.turn += 1


board_1 = fh.deserialize("gunhild", "feltet")
board_2 = fh.deserialize("pc", "pog")
test_game = Game(board_1, board_2)
test_game.shoot(0, ["1", "b"])
