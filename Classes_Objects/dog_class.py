class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
    def bark(self):
        print('Woof')
        
    def describe(self):
        print(f'{self.name} is a {self.age} years old {self.breed}')
        
    def birthday(self):
        self.age += 1
        print(f"It's {self.name}'s birthday today. {self.name} is now {self.age}")
        
dog1 = Dog('Bingo', 7, 'Beagle')
dog2 = Dog('Spikey', 11, 'Golden Retriever')
dog3 = Dog('Winny', 4, 'bulldog')
    
dog1.bark()
dog2.bark()
dog3.bark()

dog1.describe()
dog2.birthday()

dog4 = Dog('Haley', 5, 'German Shephard')
dog4.birthday()
dog4.describe()