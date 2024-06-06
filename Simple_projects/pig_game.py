import random

def roll():
    return random.randint(1, 6)

def playGame(players_scores):
    while True:
        for player in players_scores:
            print(f"{player}'s turn")
            while True:
                try:
                    choice = int(input("Options:\n1.Roll the dice or 2.Stop: "))
                except ValueError:
                    print("Enter numbers 1 or 2")
                    continue
                
                if choice == 1:
                    roll_dice = roll()
                    print(f"{player} rolled {roll_dice}")
                    if roll_dice == 1:
                        print("You rolled 1, no score for this round")
                        break
                    else:
                        players_scores[player] += roll_dice
                        print(f"Your score is {players_scores[player]}")
                        if players_scores[player] >= 50:
                                print(f"{player} wins with a score of {players_scores[player]}!")
                                print(players_scores)
                                return
                elif choice == 2:
                    break
        print(players_scores)


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
    playGame(players_scores)
    
if __name__ == "__main__":
    main()