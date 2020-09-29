import cmd
import funcs as f
import fight_funcs as ff
import file_handler as fh


class Start_menue(cmd.Cmd):
    intro = "Welcome to the shipsweeper-game!"
    prompt = "Main menue: "

    def do_make_player(self, arg):
        'Create a player: make_player player_name'
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
        print(fh.player_boards(arg))

    def do_start_pve(self, arg):
        'Start a game vs computer: player_name, player_board'
        pve(arg)
        Pve_loop().cmdloop()

    def do_start_pvp(self, arg):
        'Start game: player1, board1, player2, board2'
        pvp(arg)
        Pvp_loop().cmdloop()

    def do_show_logg(self, arg):
        'Prints the statistics for previous games'
        fh.show_logg()

    def do_quit(self, arg):
        'Exit the game'
        return True


# Initialize the pve loop
def pve(arg):
    player1, board1 = f.parse(arg)
    board1 = fh.deserialize(player1, board1)
    Pve_loop.bot = ff.Bot_player()
    board2 = Pve_loop.bot.board
    Pve_loop.game = ff.Game(board1, board2, False)
    Pve_loop.players = [player1, "pc"]


# Initialize the pvp loop
def pvp(arg):
    player1, board1, player2, board2 = f.parse(arg)
    board1 = fh.deserialize(player1, board1)
    board2 = fh.deserialize(player2, board2)
    Pvp_loop.game = ff.Game(board1, board2, True)
    Pvp_loop.players = [player1, player2]


class Pvp_loop(cmd.Cmd):
    intro = "Game starts!"
    prompt = "Player1: "
    game = object
    players = []

    def do_shoot(self, arg):
        'Shoot at other player by coordinate: shoot a1'
        self.game.shoot_who(self.prompt, arg)
        self.after_move_check()
        return self.game_over()

    def do_hp(self, arg):
        'Show remaining hp for both players'
        print(
            f"Player 1 has {self.game.hp[0]} hp left\n"
            f"Player 2 has {self.game.hp[1]} hp left"
            )

    def after_move_check(self):
        self.turn_check()

    def turn_check(self):
        if self.game.turn % 2 != 0:
            self.prompt = "player1: "
        else:
            self.prompt = "player2: "

    def game_over(self):
        if self.game.game_over:
            if "2" in self.prompt:
                players = self.players[::-1]
            else:
                players = self.players
            End_screen(players, self.game).cmdloop()
            return True

    def do_quit(self, arg):
        'Exit, game will not be logged'
        return True


class Pve_loop(cmd.Cmd):
    intro = "Playing against bot"
    prompt = "Player1: "
    game = object
    bot = object
    players = []

    def do_shoot(self, arg):
        'Shoot at other player by coordinate: shoot a1'
        self.game.shoot_who(self.prompt, arg)
        self.after_move_check()
        return self.game_over()
        # If game_over, it will return True, which breaks the loop

    def do_hp(self, arg):
        'Show remaining hp for both players'
        print(
            f"Player 1 has {self.game.hp[0]} hp left\n"
            f"Player 2 has {self.game.hp[1]} hp left"
            )

    def do_quit(self, arg):
        'Exit the game'
        return True

    def after_move_check(self):
        self.turn_check()

    def turn_check(self):
        if self.game.turn % 2 != 0:
            self.prompt = "player1: "
        else:
            self.prompt = "player2: "
            self.bot_turn()

    def bot_turn(self):
        bot_choi = self.bot.fire()  # Bots choice of coords
        print(f"player 2: shoot {bot_choi[0] + bot_choi[1]}")
        self.do_shoot(bot_choi)

    def game_over(self):
        if self.game.game_over:
            if "2" in self.prompt:
                players = self.players[::-1]
            else:
                players = self.players
            End_screen(players, self.game).cmdloop()
            return True


class End_screen(cmd.Cmd):
    intro = str
    prompt = str
    winner = str
    loser = str

    def __init__(self, players, game):
        super().__init__()
        self.winner = players[0]
        self.loser = players[1]
        self.prompt = f"🟉 {self.winner} 🟉 : "
        self.game = game
        self.logg_results()
        self.intro = (
            f"Congratulations, {self.winner}\n"
            f"{self.winner} won in {self.game.turn} turns!\n"
        )

    def do_quit(self, arg):
        return True

    def logg_results(self):
        fh.logg_game(self.winner, self.loser, self.game.turn)


Start_menue().cmdloop()
