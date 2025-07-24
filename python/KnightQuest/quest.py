########### 1.3 ##########
import pgzrun # imports the pgzrun module

# Define the height & width of the game grid & size of each grid tile
GRID_WIDTH = 16 # defines how many squares wide the game bord is 
GRID_HEIGHT = 12 # defines how many squares tall the game board is
GRID_SIZE = 50

# Define the size of of the game window
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
############################

MAP = ["WWWWWWWWWWWWWWWW",
       "W              W",
       "W              W",
       "W W  KG        W",
       "W WWWWWWWWWW   W"
       "W              W",
       "W      P       W",
       "W  WWWWWWWWW   W",
       "W      GK   W  W",
       "W              W",
       "W              W",
       "WWWWWWWWWWWWWWWW"]
       
       
       
       
    
# this function converts a grid position to screen coordinates
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

# this function draws the dungeon floor on the screen
def DrawBackground():
    for y in range(GRID_HEIGHT): # loops through every tile on the board
        for x in range(GRID_WIDTH):
            screen.blit("floor1", GetScreenCoords(x, y))
            
 
def DrawScenery():
     for y in range(GRID_HEIGHT):
         for x in range(GRID_WIDTH):
             square = MAP[y][x]
             if square == "Q":
                 screen.blit("wall", GetScreenCoords(x, y))
             elif square == "D":
                 screen.blit("door", GetScreenCoords(x, y))
                
                 
# draw() is
def Draw():
    screen.clear
    DrawBackground()
    DrawScenery()
#######################

pgzrun.go()