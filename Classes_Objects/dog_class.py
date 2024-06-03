class Dog: # Class Definition
    species = 'Canis lupus' # Class variable
    
    # Initializer / Instance Attributes
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        
    def __str__(self):
        return(f'{self.name} is a {self.age} year old {self.breed}')
        
    def __eq__(self):
        return self.name == other.name and self.age == other.age and self.breed == other.breed
    
    # Methods
    def bark(self):
        print('Woof')
        
    def describe(self):
        print(f'{self.name} is a {self.age} years old {self.breed}')
        
    def birthday(self):
        self.age += 1
        print(f"It's {self.name}'s birthday today. {self.name} is now {self.age}")

# Instantiating the Dog class      
dog1 = Dog('Bingo', 7, 'Beagle')
dog2 = Dog('Spikey', 11, 'Golden Retriever')
dog3 = Dog('Winny', 4, 'bulldog')
  
# Accessing Attributes  
dog1.bark()
dog2.bark()
dog3.bark()

# Accessing Methods
dog1.describe()
dog2.birthday()

dog4 = Dog('Haley', 5, 'German Shephard')
dog4.birthday()
dog4.describe()

# Accessing class variable
print(Dog.species)
print(dog3.species)

# Inheritance
class puppy(Dog):
    def __init__(self, name, age, breed, training_level = "beginner"):
        super().__init__(name, age, breed)
        self.training_level = training_level
        
    def bark(self):
        print('Yip')
        
dog5 = puppy('suzy', 1, 'poodle')

dog5.bark()
print(dog5.species)
dog5.describe()