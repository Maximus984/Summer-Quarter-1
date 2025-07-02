import random

players = ["kamari" , "max" , "braylen"
           , "ollie" , " xavier" , "Avery"
           , "carl" , "walter" , "darren"
           , "EJ" , "Nahuh", "joaquin"
           , "Marshawn" , "ja'den" , "isaiah"
           , "kenlon" , "Nishad" , "Kauri"
           , "kriss" , "Joseph" , "semaj"
           , "tay" , "taqari" , "jarma"]

def PickTeams(players):
    random.shuffle(players)
    team1 = players[:len(players)//2]
    teamCaptain1 = team1[random.randrange(0, 12)]
    
    team2 = players[len(players)//2:]
    teamCaptain2 = team2[random.randrange(0, 12)]
    
    print("TEAM 1:")
    print("Team 1 Captain: " + teamCaptain1)
    for player in team1:
        print(player)
    
    print("\nTEAM 2:")
    print("Team 2 Captain: " + teamCaptain2)
    for player in team2:
        print(player)   
        
PickTeams(players)

