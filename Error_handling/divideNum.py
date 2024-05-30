def divide_numbers():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        result = numerator / denominator

        print("Result of division:", result)

    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        divide_numbers()

    except ValueError:
        print("Please enter valid numeric values.")
        divide_numbers()

divide_numbers()