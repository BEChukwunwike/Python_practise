import math

# Function to print the circumference of a circle
def print_circum(radius):

    circle_circumference = 2 * math.pi * radius
    rounded_circumference = round(circle_circumference,5)
    print("The circumference of a circle of radius " + str(radius) + " is " + str(rounded_circumference) + ".")

# Function call with different values for radius.
print_circum(6)
print_circum(3.5)
print_circum(8)