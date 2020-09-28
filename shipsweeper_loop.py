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
        f.make_board(arg)

    def do_modify_board(self, arg):
        pass

    def do_see_players(self, arg):
        pass

    def do_see_boards(self, arg):
        'See which boards a player has: see_boards player_name'
        fh.player_boards(arg)

    def do_start_pve(self, arg):
        'Start a game vs computer: player_name, player_board'
        farg = ("gunhild", "feltet")
        pve(farg)
        Pve_loop().cmdloop()

    def do_start_pvp(self, arg):
        'Start game: player1, board1, player2, board2'
        arga = ("gunhild","feltet","gustav","level_one")
        pvp(arga)
        Pvp_loop().cmdloop()

    def do_quit(self, arg):
        'Exit the game'
        return True


def pve(arg):
    player1, board1 = arg
    board1 = fh.deserialize(player1, board1)
    Pve_loop.bot = ff.Bot_player()
    board2 = Pve_loop.bot.board
    Pve_loop.game = ff.Game(board1, board2, False)


def pvp(arg):
    player1, board1, player2, board2 = arg
    board1 = fh.deserialize(player1, board1)
    board2 = fh.deserialize(player2, board2)
    Pvp_loop.game = ff.Game(board1, board2, True)


class Pvp_loop(cmd.Cmd):
    intro = "Game starts!"
    prompt = "Player1: "
    game = object

    def do_shoot(self, arg):
        self.game.shoot_who(self.prompt, arg)
        self.turn_check()

    def turn_check(self):
        if self.game.turn % 2 != 0:
            self.prompt = "player1: "
        else:
            self.prompt = "player2: "
        if self.game.game_over is True:
            print("something")


class Pve_loop(cmd.Cmd):
    intro = "aaa"
    prompt = "Player1: "
    game = object
    bot = object

    def do_shoot(self, arg):
        self.game.shoot_who(self.prompt, arg)
        self.turn_check()

    def turn_check(self):
        if self.game.turn % 2 != 0:
            self.prompt = "player1: "
        else:
            self.prompt = "player2: "
            bot_turn()
    
    def bot_turn(self):
        self.game.shoot_who(self.prompt, self.bot.fire())
        




Start_menue().cmdloop()
