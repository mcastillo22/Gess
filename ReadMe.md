# Gess

Gess is a variant of the games Chess and Go. Further details of the game can be found [here](https://en.wikipedia.org/wiki/Gess).
<p align="center">
<img src="https://raw.githubusercontent.com/mcastillo22/Gess/master/Screenshots/example.gif"><img src="https://raw.githubusercontent.com/mcastillo22/Gess/master/Screenshots/WinEx.gif"> 
</p>

## Prerequisites:
* This game can be played using GUI
* Requires Python3
* Python3 installation instructions can be found [here](https://realpython.com/installing-python/)

## Getting Started:
* Download all files (not including Screenshots folder)
* Run main.py to play
  * For example: open a new command line and navigate tothe directory where files have been downloaded
* Type `python3 main.py` and hit `Enter`

# Gameplay:
* Blue stones go first
* Each player begins with 43 stones
* Players choose a **piece** to move

## Pieces:
* A piece consists of the stones in a 3x3 grid (called a *footprint*)
  * Clicking a space on the grid will highlight the current piece selected.
  * The spot clicked will become the center of the piece
* The piece must only consist of stones belonging to that player
* The stone configuration of the piece determines what direction and how many spaces that piece can move
* A piece with a center stone can move unlimited spaces, barring no stones block that piece's path
* Otherwise, a piece can move a max of 3 spaces from its center
* A piece can move to the edge of the board; however, any stones on the edge of the board 'fall off'