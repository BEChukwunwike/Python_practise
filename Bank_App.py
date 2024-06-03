class Bank_Accouts:
    Acct_db = []
    def __init__(self, name, acct_num, initial_deposit = 0):
        self.name = name
        self.acct_num = acct_num
        self.balance = initial_deposit
        Bank_Accouts.Acct_db.append(self)
        print("\n Hello ", self.name)
        
    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount, "New Balance: ", self.balance)
        
    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if amount > self.balance:
            print("\n Insufficient balance")
        else:
            self.balance -= amount
            print("\n You Withdrew:", amount, "New Balance: ", self.balance)
        
    def display(self):
        print("\n Available Balance=", self.balance)
        
        
def main():
    while True:
        print("\nChoose your service below")
        print("\n1. Create New account")
        print("\n2. Deposit")
        print("\n3. Withdrwaw")
        print("\n4. Check Balance")
        print("\n5. Exit")
        
        try:
            choice = int(input("\nEnter your choice: "))
            break
        except:
            print("\nEnter numbers between 1-5")
            
            
        
        if choice == 1:
            name = input("\nEnter your name: ")
            acct_num = int(input("\nEnter your account number: "))
            initial_deposit = float(input("\nEnter your initial deposit: "))
            
            account = Bank_Accouts(name, acct_num, initial_deposit)
        elif choice == 2:
            account.deposit()
        
        elif choice == 3:
            account.withdraw()
            
        elif choice == 4:
            account.display()
            
        elif choice == 5:
            break
        
        else:
            print("\nInvalid input")
            
if __name__ == "__main__":
    main()