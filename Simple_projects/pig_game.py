import random

def roll():
    return random.randint(1, 6)

player_dict = {}


def main():
    print("Welcome to the Pig Game")
    while True:
        try:
            players = int(input("How many players? \nChoose 2 - 4: "))
        except ValueError:
            print("Enter numbers between 2 - 4")
            continue
        if players in range(2, 5):
            break
        else:
            print("Enter numbers between 2 - 4")
            continue
        
    players_scores = {}
    for i in range(1, players + 1):
        player_name = input(f"Enter the name for player {i}: ")
        players_scores[player_name] = 0
    
        
    print(players_scores)
    
        
            
    
if __name__ == "__main__":
    main()