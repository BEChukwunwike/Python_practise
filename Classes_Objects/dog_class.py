class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
    def bark(self):
        print('Woof')
        
dog1 = Dog('Bingo', 7, 'Beagle')
dog2 = Dog('spikey', 11, 'Golden Retriever')
dog3 = Dog('Winny', 4, 'bulldog')
    
dog1.bark()
dog2.bark()
dog3.bark()