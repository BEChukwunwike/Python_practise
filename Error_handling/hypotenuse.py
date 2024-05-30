import math

def hypotenuse(leg1=None, leg2=None):
    try:
        # Check if both arguments are provided
        if leg1 is None or leg2 is None:
            raise ValueError("Both leg1 and leg2 must be provided.")

        # Check if both arguments are positive numbers
        elif leg1 <= 0 or leg2 <= 0:
            raise ValueError("Both legs must be positive numbers.")

        # Calculate and print the squares of legs
        else:
            leg1_squared = leg1 ** 2
            leg2_squared = leg2 ** 2


            # Calculate the length of the hypotenuse using Pythagorean theorem
            hypotenuse_length = math.sqrt(leg1_squared + leg2_squared)
            return hypotenuse_length

    except ValueError as e:
        print("Error:", e)

# Test with different arguments
test_arguments = [(3, 4), (15, 0), ()]
for legs in test_arguments:
    print("Testing with arguments:", legs)
    print(hypotenuse(*legs))
    print()

