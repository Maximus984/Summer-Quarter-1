def RPS():
    print("Welcome to Rock, Paper, Scissors!")
    player1 = input("player 1, please enter your name: ")
    player2 = input("player 2, please enter your name: ")
    
    p1_choice = input(f"{player1}, please choose Rock, Paper, or Scissors: ")
    
    while not LsValioMove(p1_choice):
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        p1_choice = input(f"{player1}, please choose Rock, Paper, or Scissors: ")
    
    p2_choice = input(f"{player2}, please choose Rock, Paper, or Scissors: ")

    while not LsValioMove(p2_choice):
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        p2_choice = input(f"{player2}, please choose Rock, Paper, or Scissors: ")

    if p1_choice == "rock" and p2_choice == "scissors":
        print(f"rock beats scissors, {player1} wins!")
    elif p1_choice == "scissors" and p2_choice == "paper":
        print(f"scissors beats paper, {player1} wins!")
    elif p1_choice == "paper" and p2_choice == "rock":
        print(f"paper beats rock, {player1} wins!")
    
    elif p1_choice == p2_choice:
        print("It's a tie!")
    else:
        print(f"{player2} wins!")
    
def LsValioMove(playerMove):
    valioMoves, = ["rock", "paper", "scissors"]

    if playerMove.lower() in valioMoves:
        return True
    else:
        return False



    
    
RPS()