def make_positive(number):
    if not isinstance(number, (int, float)):
        return("Input must be a numeric value")
    
    elif number < 0:
        return -number  # Returns the absolute value for negative numbers
    elif number == 0:
        return 1  # Return 1 for zero input (assuming positive 1)
    return number


print(make_positive("7"))
