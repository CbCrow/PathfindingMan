#   Collin Crowthers     20 April 2021
#   Pacman-like maze game to show use of the 
#   A* pathfinding algorithm
#

Write a Pac-Man liked game. The game board is tiled. 
The movement of Pac-Man is to be controlled by the game player and the movement of the ghost(s) 
is to be controlled by the program.  
Both Pac-Man and the ghost(s) can only move up, down, left, or right one tile position at a time. 
 No diagonal movement is allowed. 

Movement can be accomplished using the WASD or arrow keys
The player is yellow and the ghost is green.

The ghost uses A* pathfinding to get to pacman and its path is highlighted in red

The A* algorithm uses the heuristic of estimated distance to inform its decision
to what path to look through. I have done this based on the amount of vertical and horizontal moves
that would be needed if no barrier existed. This is combined with the previously travelled distance
in order to find new squares for the path to take.