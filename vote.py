def vote(citizen, age):
    if citizen:
        if age >= 18:
            print("You are eligible to vote.")
        else:
                print("You must be 18 or older to vote.")
    else:
        print("You must be a citizen to vote.")
        
vote(True, 21)