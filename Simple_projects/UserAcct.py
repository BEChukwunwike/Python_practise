class UserAccount:
    userList = []
    def __init__(self, fName, lName, country, state, password):
        self.fName = fName
        self.lName = lName
        self.country = country
        self.state = state
        self.password = password
        self.update_user_dict()
        
    def update_user_dict(self):
        self.user_dict = {
            "first_name": self.fName,
            "last_name": self.lName,
            "country": self.country,
            "state": self.state,
            "password": self.password
        }
        
    def getFullName(self):
        return self.fName + " " + self.lName
    
    def validate_password(self):
        charType = {
            "uppercase" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "lowercase" : "abcdefghijklmnopqrstuvwxyz",
            "specialChar" : "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~",
            "number" : "1234567890"
            }
        countChar = {"uppercase": 0, "lowercase": 0, "specialChar": 0, "number": 0}
        if len(self.password) >= 8:
            for char in self.password:
                if char in charType["lowercase"]:
                    countChar["lowercase"] +=1
                elif char in charType["uppercase"]:
                    countChar["uppercase"] +=1
                elif char in charType["specialChar"]:
                    countChar["specialChar"] +=1
                elif char in charType["number"]:
                    countChar["number"] +=1
                    
            if all(value > 0 for value in countChar.values()):
                return True
            else:
                print("Invalid Password: Password must contain at least one lowercase letter, one uppercase letter, one special character, and one number.")
                return False
        else:
            print("Invalid Password: Password must be at least 8 characters long")
            return False
            
                
    def userUpdate(self):
        print("Update your account details")
        self.fName = input("Enter your first name: ")
        self.lName = input("Enter your last name: ")
        self.country = input("Enter your country: ")
        self.state = input("Enter your state: ")
        self.update_user_dict()
        
    def reset_password(self):
        while True:
            self.password = input("Enter your new password: ")
            if self.validate_password():
                self.update_user_dict
                print("Password reset successful")
                break
            else:
                print("Password reset failed")
                
    def displayUser(self):
        print(f"Full Name: {self.getFullName()}\nCountry: {self.country}\nState: {self.state}")
        
    
def main():
    createAccount = input("Welcome To mySocials: Want to create an account? y/n: ")
    if createAccount.lower() == "y":
        fName = input("Enter your first name: ")
        lName = input("Enter your last name: ")
        country = input("Enter your country: ")
        state = input("Enter your state: ")
        password = input("Enter your password: ")
        newUser = UserAccount(fName, lName, country, state, password)
        if newUser.validate_password():
            UserAccount.userList.append(newUser.user_dict)
            print("Account created successfully")
        else:
            print("Account creation failed")
    else:
        print("Thank you for visiting mySocials")
    
    if UserAccount.userList:
        updateUser = input("Want to update your profile info? y/n: ")
    
    if updateUser.lower() == "y":
        for user_dict in UserAccount.userList:
            user = UserAccount(
                    user_dict["first_name"],
                    user_dict["last_name"],
                    user_dict["country"],
                    user_dict["state"],
                    user_dict["password"]
                )
            user_dict.displayUser()
            user_dict.userUpdate()
            user_dict.displayUser()
            user_dict.reset_password()
            user_dict.displayUser()
    else:
        print("Thank you for visiting mySocials")
        
if __name__ == '__main__':
        main()