#   Collin Crowthers     20 April 2021
#   Pacman-like maze game to show use of the 
#   A* pathfinding algorithm
#

import pygame

# class for nodes for pathfindiing
class Node:

    def __init__(self, inPos, parentA):
        self.f = 0 # combined values
        self.g = 0 # distance to goal
        self.h = 0 # actual cost
        self.pos = inPos # position...
        self.parent = parentA

    #finds distance between self and position
    def getDistance(self, pos1):
        x1, y1 = self.pos
        x2, y2 = pos1
        return abs(x1 - x2) + abs(y1 - y2)

    def __eq__(self, other):
        return self.pos[0] == other.pos[0] and self.pos[1] == other.pos[1]


# pathfinding algorithm
def aStar(grid, start, end):
    #initialize lists
    openSet = []
    closedSet = []
    #add start node in open list
    startNode = Node(start, None)
    endNode = Node(end, None)
    openSet.append(startNode)

    #loop until end node
    while len(openSet)>0:
        # get node with smallest f value by sorting 
        openSet.sort(key=lambda Node: Node.f)
        currentNode = openSet[0]
        openSet.pop(0)
        closedSet.append(currentNode)

        #if current node position is the end position...
        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.pos)
                current = current.parent
            print (path)
            return path
            
        #check around the square
        child = []
        for newPossible in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nodePosition = (currentNode.pos[0] + newPossible[0], currentNode.pos[1] + newPossible[1])
            if nodePosition[0] > 19 and nodePosition[0] < 0 or nodePosition[1] > 19 and nodePosition[1] < 0:
                continue
                
            print (nodePosition[0], nodePosition[1])
            if grid[nodePosition[0]][nodePosition[1]] == 1: 
                continue

            newNode = Node(nodePosition, currentNode)
            child.append(newNode)

        for children in child:
            # on the closed list
            for each in closedSet:
                if children == each:
                    continue

            # generate the f, g, and h values
            children.g = currentNode.g +1
            children.h = children.getDistance(end)
            children.f = children.g + children.h

            # already in the open list
            for each in openSet:
                if children == each and children.g > each.g:
                    continue

            openSet.append(children)




 
# color variables
Black = (0, 0, 0)       # used for background/empty
White = (255, 255, 255) # used for pellets
Green = (0, 255, 0)     # used for ghost
Red = (255, 0, 0)       # used for ghost pathfinding
Blue = (0, 0, 255)      # used for walls
Yellow = (255, 255, 0)
 
# sets size and spacing
gridWidth = 20
gridHeight = 20
between = 5
 
# create game map, walls are 1, empty is 0, pacman is 2, ghost is 3, 10 is a path
grid = [[ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]

#set pacman starting position and ghost
pacmanrow = 1
pacmancolumn = 2
newrow = 0
newcolumn = 0
grid[pacmanrow][pacmancolumn] = 2

ghostrow = 10
ghostcolumn = 10
grid[ghostrow][ghostcolumn] = 3

# Initialize pygame
pygame.init()
# screen size
WINDOW_SIZE = [505, 505]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Pathfinding Game")
# Loop until the user clicks the close button.
quit = False
clock = pygame.time.Clock()
 
# main
while not quit:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  # if time to exit
            quit = True  
        
        #movement type set
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                newrow = pacmanrow
                newcolumn = pacmancolumn-1
                if newcolumn == -1:
                    newcolumn = 19

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                newrow = pacmanrow
                newcolumn = pacmancolumn+1
                if newcolumn == 20:
                    newcolumn = 0

            if event.key == pygame.K_UP or event.key == ord('w'):
                newrow = pacmanrow-1
                newcolumn = pacmancolumn

            if event.key == pygame.K_DOWN or event.key == ord('s'):
                newrow = pacmanrow+1
                newcolumn = pacmancolumn

        if event.type == pygame.KEYUP:
            #movement will now occur
            grid[pacmanrow][pacmancolumn] = 0
            grid[ghostrow][ghostcolumn] = 0
            #if valid movement change position based on new 
            if newrow < 20 and newrow >= 0 and newcolumn < 20 and newcolumn >= 0 and grid[newrow][newcolumn] != 1:
                pacmanrow = newrow
                pacmancolumn = newcolumn
                
                ## because a change has occured, ghosts should now process this movement
                start = [ghostrow, ghostcolumn]
                end = [pacmanrow, pacmancolumn]
                path = aStar(grid, start, end)
                for row in range(20):
                    for column in range(20):
                        if grid[row][column] == 10:
                            grid[row][column] = 0
                for each in path:
                    grid[each[0]][each[1]] = 10

                #now let the ghost move
                if grid[ghostrow+1][ghostcolumn] == 10:
                    ghostrow += 1
                elif grid[ghostrow-1][ghostcolumn] == 10:
                    ghostrow += -1
                elif grid[ghostrow][ghostcolumn+1] == 10:
                    ghostcolumn += 1
                elif grid[ghostrow][ghostcolumn-1] == 10:
                    ghostcolumn += -1

            
            grid[pacmanrow][pacmancolumn] = 2
            grid[ghostrow][ghostcolumn] = 3
 
    # background to black
    screen.fill(Black)
 
    # Draw the array
    for row in range(20):
        for column in range(20):
            color = Black
            if grid[row][column] == 1:
                color = Blue
            elif grid[row][column] == 2:
                color = Yellow
            elif grid[row][column] == 3:
                color = Green
            elif grid[row][column] == 10:
                color = Red
            pygame.draw.rect(screen,color,[(between + gridWidth) * column + between,
                            (between + gridHeight) * row + between, gridWidth,gridHeight])
 
    # 60fps
    clock.tick(60)
    # update screen
    pygame.display.flip()
 
pygame.quit()


    
        

