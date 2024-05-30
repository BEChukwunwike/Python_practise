food_classes = ['Vegetables', 'Fruits', 'Grains', 'Protein Foods', 'Dairy']

# Using enumerate to get index and food class
for index, food_class in enumerate(food_classes, start=1):
    print("Class", index,":", food_class)
