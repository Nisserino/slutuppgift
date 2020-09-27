import cmd
import funcs as f
import fight_funcs as ff
import file_handler as fh


class Start_menue(cmd.Cmd):
    intro = "Welcome to the shipsweeper-game!"
    prompt = "Player: "

    def do_make_player(self, arg):
        'Create a player'
        f.make_player(arg)

    def do_make_board(self, arg):
        'Make a board for an existing player: player_name, board_name'

    def do_modify_board(self, arg):
        pass

    def do_see_players(self, arg):
        pass

    def do_see_boards(self, arg):
        pass

    def do_start_game(self, arg):
        'Start game: player1, board1, player2, board2'
        arga = ("gunhild","feltet","gustav","level_one")
        fake_init(arga)
        Game_loop().cmdloop()

    def do_quit(self, arg):
        'Exit the game'
        return True


class player_1(cmd.Cmd):
    intro = "Let's blow up some ships!"
    prompt = "Player1: "

    def do_shoot(self, arg):
        pass

    def do_quit(self, arg):
        'Exit the game'
        return True


class player_2(cmd.Cmd):
    prompt = "Player2: "

    def do_shoot(self, arg):
        'shoot at coordinate, ie: a1,b1'
        pass


def fake_init(arg):
    player1, board1, player2, board2 = arg
    board1 = fh.deserialize(player1, board1)
    board2 = fh.deserialize(player2, board2)
    Game_loop.game = ff.Game(board1, board2)


class Game_loop(cmd.Cmd):
    intro = "Game starts!"
    prompt = "Player1: "
    game = object

    def do_start(self, arg):
        self.turn_check()

    def do_shoot(self, arg):
        self.game.shoot_(self.prompt, arg)
        self.turn_check()

    def turn_check(self):
        if self.game.turn % 2 != 0:
            self.prompt = "player1: "
        else:
            self.prompt = "player2: "


Start_menue().cmdloop()
