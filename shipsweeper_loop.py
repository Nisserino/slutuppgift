import cmd
import funcs as f


class Start_menue(cmd.Cmd):
    intro = "Welcome to the shipsweeper-game!"
    prompt = "Player: "

    def do_make_player(self, arg):
        'Create a player'
        f.make_player(arg)

    def do_make_board(self, arg):
        pass

    def do_modify_board(self, arg):
        pass

    def do_see_players(self, arg):
        pass

    def do_see_boards(self, arg):
        pass

    def do_start_game(self, arg):
        pass

    def do_quit(self, arg):
        'Exit the game'
        return True


class Game_loop(cmd.Cmd):
    intro = "Let's blow up some ships!"
    prompt = "Player: "

    def do_quit(self, arg):
        'Exit the game'
        return True


Start_menue().cmdloop()
