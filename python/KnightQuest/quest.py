########## 1.3 ##########
# Import the Pygame module to start using its functions
import pgzrun 
# Define width and height of the game grid & size of each grid tile 
GRID_WIDTH = 27  # defines How many squares wide the game board is 
GRID_HEIGHT = 12 # defines How many squares tall the game board is 
GRID_SIZE = 50 
GUARDMOVEINTERVAL = 0.20
# Define the size of the game window
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
PLAYER_MOVE_INTERVAL = 0.1 # time it takes 
#########################
########## 1.5 ##########
MAP = ["WWWWWWWWWWWWWWWWWWWWWWWWWWW",
       "W  W K   G    W kk      K W",
       "W           W    w   W    W",
       "W  W  K    W              W",
       "W  WWW WWWWWW kk   K WW   W",
       "W  W  W      WWW          W",
       "W  K   P   k   WWWWW      W",
       "W  WWWWWWWWWW       K     W",
       "W       K   W  K   WWW    W",
       "W  W        WWW           W",
       "W     G   W K  WW WWW  K  W",
       "WWWWWWWWWWWWWWWWWDWWWWWWWWW"]
#########################
########## 1.4 ##########
# This function converts a grid position to screen coordinates
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)
# This function draws the dungeon floor as a background on screen
def DrawBackground():
    for y in range (GRID_HEIGHT): # loop over each grid row
        for x in range (GRID_WIDTH): # loop over each grid column
        if x % 2 == y % 2:
            #Draw the floor 1 panel
            screen.blit("floor1", GetScreenCoords(x, y)) # Draws the named imaged at the given screen position
        else:
            screen.blit("floor2", GetScreenCoords(x, y))
#########################
########## 2.1 ##########
# This function takes in an actor as an argument & 
# returns the postion of the actor on the grid
def GetActorGridPos(actor):
    return(round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))
#########################
########## 1.7, 3.0, 3.3 ##########
# This function creates an actor object from the Actor class to reperesent the player & keys
def SetupGame():
    global player # Define player as a global var that be accessed anywhere in your code
    global keysToCollect # A var to store all the keys the player needs to collect
    global gameOver
    global guards
    global playerWon

    
    player = Actor("player", anchor=("left", "top")) # Create a new Actor & set its anchor
    keysToCollect = []
    gameOver = False
    guards = []
    playerWon = False
    
    for y in range(GRID_HEIGHT): # Loop over each grid position 
        for x in range(GRID_WIDTH):
            square = MAP[y][x] # Extracts the character from the MAP variable
            if square == "P": # Checks if the grid position is the player
                player.pos = GetScreenCoords(x, y) # Set the position of the player
            elif square == "K": 
                # Create an actor for that key
                key = Actor("key", anchor=("left", "top"))
                # Set the key's pos to this grid location
                key.pos = GetScreenCoords(x, y)
                # Add this key to our list of keys
                keysToCollect.append(key)
            elif square == "G":
                #create a guard actor
                guard = Actor("guard",anchor=("left", "top"), pos = GetScreenCoords(x, y))
                #add this key to our list of guards
                guards.append(guard)
#########################
########## 1.6 ##########
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))
########## 1.8, 3.1 ##########
def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
    for guard in guards:
        guard.draw()
############################
def DrawGameOver():
    #Calculate and store the middle pos of the the game screen
    screenMiddle = (WIDTH / 2, HEIGHT / 2)
    # Drraw "Game Over" on the screen
    screen.draw.text("GAME OVER" , midbottom = screenMiddle,
                     fontsize = GRID_SIZE, color="cyan", owidth=1)

    # Check if the player won the game or not
    if playerWon:
        # draw a you win message on screen 
        screen.draw.text("YOU WIN", midtop = screenMiddle,
                         fontsize = GRID_SIZE, color = "green", owidth=1)
    # else meaning the player lost the game 
    else:
        # draw a you lose message on screen
        Screen.draw.text("YOU LOSE!", midtop = screenMiddle,
                         fontsize = GRID_SIZE, color = "red", owidth=10)


# Draw the restart message on screen
    Screen.darw.text("Press space to play again",
                 midtop=(WIDTH/2, HEIGHT/2 + GRID_SIZE),
                 fontsize=GRID_SIZE/2,
                 color="cyan", owidth=0)







#############################
# draw() is 
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        DrawGameOver()
    
#########################
###########5.3##############
def on_key_up(key):
    # check if the space bar has been pressed once the game is over
    if key == keys.SPACE and gameOver:
        # reset the game
        SetupGame
###############################



########## 2.2, 3.2 ##########
def MovePlayer(dx, dy):
    global gameOver
    global playerWon
    if gameOver: # if the game is over
        # stop the player from stopping the rest of the move functio
        return # do no let the player exit the door if there are keys left
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP[y][x]
    if square == "W": # If the player tries to move into a wall
        return # stop the function, dont let the player move
    elif square == "D":
        if len(keysToCollect) > 0: # If there are keys left to collect
            return  # do no let the player exit the door if there are keys left
        else:
            gameOver = True # End the game
            plaeyerWon = True
    for key in keysToCollect:
        # Get the grid pos of the current key
        (keyX, keyY) = GetActorGridPos(key) 
        # Check if the new player pos mathces the pos of one of the keys
        if x == keyX and y == keyY: # if the player is moving to the same pos as the key
            #remove the key from the keys list
            keysToCollect.remove(key)
            break
        animate(player, pos=GetScreenCoords(x, y),
                duration=PLAYER_MOVE_INTERVAL)
        # DELETE LINE BELOW
        #player.pos = GetScreenCoords(x,y)
#########################

def MoveGuard(guard):
    global gameOver
    if gameOver: # if the game is ove
        return # do nothing and end this function call
    
    # get the x & y grid pos of the player
    (playerX, playerY) = GetActorGridPos(player)
    # get teh x & y grid pos of the guard
    (guardX, guardY) = GetActorGridPos(guard)
    
    # check if the player is to the right of the guard and if the right is not a wall
    if playerX > guardX and MAP[guardY][guardX + 1] != "W":
    # increase the guard's x grid pos by 1 to move him right
        guardX += 1
    # check if the player is to the left of the guard and if the square to the left is not a wall
    elif playerX < guardX and MAP[guardY][guardX - 1] != "W":
        # Decrease the guard's x pos by 1 to move him left
        guardX -= 1
    # check if the player is above the guard and if the square above is not a wall
    elif playerY > guardY and MAP[guardY + 1][guardX] != "W":
        # Decrase the guard's y pos by 1 to move him down
        guardY += 1
    elif playerY < guardY and MAP[guardY - 1][guardX] != "W":
        guardY -=1
        
    # Animate the guaed as he moves
    animate(guard, pos=GetScreenCoords(guardX, guardY),
            duration=GUARDMOVEINTERVAL)
    
    # DELETE THE BELOW LINE OF CODE
    #guard.pos = GetScreenCoords(guardX, guardY)
        
    # Update the guard actor's pos to the screen
    guard.pos = GetScreenCoords(guardX, guardY)
    #Check if the guard has touched the player
    if guardX == playerX and guardY == playerY:
        gameOver = True # end the game
        
############4.2#######################  

def MoveGuards():
    for guard in guards:
        MoveGuard(guard)
############################
        


########## 2.3 ##########
# This Function gets a key from the user and moves the player based on the input
def on_key_down(key):
    if key == keys.LEFT: 
        MovePlayer(-1, 0) # Player moves left one on the grid
    elif key == keys.UP:
        MovePlayer(0, -1) # Player moves up one on the grid
    elif key == keys.RIGHT: 
        MovePlayer(1, 0) # Player moves right one on the grid
    elif key == keys.DOWN:
        MovePlayer(0, 1) # Player moves down one on the grid
#########################
# Start the Pygame 
SetupGame()
clock.schedule_interval(MoveGuards, GUARDMOVEINTERVAL)
pgzrun.go()
