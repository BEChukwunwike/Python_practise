import random
class Bank_Accouts:
    Acct_db = []
    def __init__(self, name, initial_deposit = 0):
        self.name = name
        self.acct_num = self.generate_acct_num()
        self.balance = initial_deposit
        Bank_Accouts.Acct_db.append(self)
        print(f"\nHello, {self.name}. Your account number {self.acct_num} is created with balance {self.balance}.")
        
    @staticmethod   
    def generate_acct_num():
        while True:
            acct_num = random.randint(1000000000, 9999999999)
            if not Bank_Accouts.find_acct(acct_num):
                return acct_num
            
        
    @classmethod
    def find_acct(cls, acct_num):
        for acct in cls.Acct_db:
            if acct.acct_num == acct_num:
                return acct
        return None
    
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
        print("\n3. Withdraw")
        print("\n4. Check Balance")
        print("\n5. Exit")
        
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nEnter numbers between 1-5")
            continue
            
        
        if choice == 1:
            name = input("\nEnter your name: ")
            initial_deposit = float(input("\nEnter your initial deposit: "))
            Bank_Accouts(name, initial_deposit)
            
        elif choice in [2,3,4]:
            acct_num = int(input("Enter your account number: "))
            account = Bank_Accouts.find_acct(acct_num)
            if account:
                if choice == 2:
                    account.deposit()
                elif choice == 3:
                    account.withdraw()
                elif choice == 4:
                    account.display()
            else:
                print("Account not found.")
        elif choice == 5:
            print("Exiting... Goodbye!...")
            break
        
        else:
            print("\nInvalid input")
            
if __name__ == "__main__":
    main()