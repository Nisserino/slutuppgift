import cmd


class Start_menue(cmd.Cmd):
    intro = "Welcome to the shipsweeper-game!"
    prompt = "Player: "

    def do_see_player(self, arg):
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
