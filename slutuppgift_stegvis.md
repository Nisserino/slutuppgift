## Steg 1
Finished in the zoom group.

## Steg 2

- 3 different indata with expected output
    1. make_board player_name, board_name
        initializing board: board_name, for player_name, let's place your boats
    2. start_game player_name, board_x, opponent_name, board_y
        Starting a game: player_name vs opponent_name
        Flipping a coin to see who starts!
    3. modify_board player_name, board_name
        Modyfying player_names board: board_name
        (print out map, with ships on it)
        Which boat would you like to move?

### I will use cmd module for input handling, and write my func accordingly

- make_board
    Will call for the function to create a board for player_x
    Will name the board: board_y

    Board will most likely be made as a numpy array.
    Will be saved to a file, might be json.

- start_game
    Want the args:
        player_name (The name of the player)
        player_board (The board bellonging to the player that they want to use)
        opponent_name (The name of the opponent, pc for is an option)
        opponent_board (The board name of the opponent)

    The program will flip a coin to see who gets to go first
    Then it will print out the boards, with the players name on top.
    The boards will be empty, hit's and misses will be registered here.
    At the bottom, a turn counter will be present.
    (game start)

- modify_board
    Want the args:
    player_name (-//-)
    board_name (-//-)
    prints out the board
    prints "Which boat would you like to move?

    You then choose a boat on the coordinate system, if there is no boat there, the program asks you to try again. 

    when a boat is selected, the program will print out the board with the boat removed from the board, and ask you where you would like to place it.
    To place the boat, give the input with the starting coordinate of the boat, and the next coordiante to tell the program which direction the boat should go. 
    the program checks that there are no collisions with other boats, and that the boat stays on the coordinate system.

## Psuedo code 

Loop together a 10x10 dataframe, col a-j, rows 1-10
fill all with 'O'
    empty_list = []
    for x in range 10 
        row = []
        for y in range 10
            append 'O' to row
        append row, as np_arr to empty list
    make pandas dataframe from empty_list
    add index 1-10
    add cols a-j

let player add boats, replace a,x-a,y with num(identifyer for boattype)
save map to saves.json
    if making new board
    place_ships(board):
        ship_4()
        for i in range 2, ship_3
        for i in range 3, ship_2
        for i in range 4, ship_1

    else
    print board
    ask for pos of ship you want to move
    check if the cells around the chosen position contains a ship
    if a cell does, do the check again
    append all finds to a temp_list
    when all cells are found, replace found positions stored in tmp_list with 'O'

    use len(tmp_list) to figure out how big a ship player can put out
    call relevant func 
    if len(tmp_list) == 3:
        ship_3()

adjacent_check(coords, board, lindex, lolumns)
    positions_allowed = True
    my_list = [-1, 1]
    for coord in coords
        ind_start = lindex.index(coord[0])
        col_start = lolumns.index(coord[1])
        
        



