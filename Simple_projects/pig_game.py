import random

def roll():
    return random.randint(1, 6)

def main():
    print("Welcome to the Pig Game")
    while True:
        try:
            players = int(input("How many players? \nChoose 2 - 4: "))
        except:
            print("Enter numbers between 2 - 4")
            continue
        if players in range(2, 4):
            break
        else:
            print("Enter numbers between 2 - 4")
            continue
        
        
            
    
if __name__ == "__main__":
    main()