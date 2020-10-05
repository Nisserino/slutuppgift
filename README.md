# Shipsweeper
Shipsweeper is a battleship game coded in python which you play in the terminal.  
You can play against a friend or against a bot.  
If you want to help out on improving the game, make a fork, or contact me!

When playing the game, if you are at any point wondering what you can do  
Write ```help``` or ```?```  
And if you're wondering how to use a specific command, such as ```show_boards```  
Write ```help show_boards``` or ```? show_boards```
## Table of Contents
1. [How to install](#How-to-install)
2. [How to run](#How-to-run)
3. [How to play](#How-to-play)



## How to install
---
Make sure you have python installed as well as pandas  
Clone this repository, and you're done!  

## How to run
---
Go to the folder you downloaded the game to in your terminal or IDE  
Run the ```shipsweeper.py``` script and get shooting

## How to play
---
>All of the actions below assumes that you are in the shipsweeper loop  
_if not check [How to run](#How-to-run)_
### __Making a player, and a board__
  
  
When staring the game for the first time, you want to make your player profile  
Write "make_player (your name)"  
And then you have an empty profile.    
Next you want to make your board.  
Write "make_board (your name), (your boards name)"  
This will send you to a menue asking you which coordinates you want to place your ships on.  
>Coordinates are for example a1, c5 or similar.  

When asked to place ships larger than 1 cell, the program expects you to give the coordinate that the ship starts on, and the second coordinate, starting with the lower one. And separated by a comma (',')  
>For example, to place a 4cell ship from a1 to a4, you would write a1,a2

If you want to play against your friend he/she will also have to make their own player profile aswell as their own board.

If you on the other hand want to play against the computer, you can start right after you made your own board.

### __Starting a game__

>Play against the computer

Write ```start_pve ```_```(your name),(board name)```_  

>Play against a friend on the same machine

Write ```start_pvp ```_```(your name),(board name),(your friends name),(his/hers board name)```_  

Now you have started playing battle ship! I mean shipsweeper.  
If you're playing against the bot, the program shoots on it's own, and whenever you can take an action, it is your turn.  

If you're playing against a friend, the first name you wrote when starting the match will be player 1, and gets to go first.
Keep a look on the prompt to see who's turn it is.  

### __In-game__

As an example, to shoot in the top left corner  
Write ```shoot a1```  
If it was a hit, you get to go again, otherwise it is your opponents turn.  

Other than shooting, to see how much hp each player has left.  
Write ```hp```  

You can also quit the game midways, but keep in mind that the game will __not__ be saved, and as the game is inconclusive, it will not be logged. If you still want to quit midway  
Write ```quit```  

### __Post-game__

When the match is finished, the program will tell you who won, and how many turns it took. It will also put you in a post-game loop where the prompt is the name of the winner.  

When you want to go back to the main menue  
Write ```quit```

The program will also logg the results for you to see later on.
To get the results, you need to be in the main menue  
Write ```show_logg```