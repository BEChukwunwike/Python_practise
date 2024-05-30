def factorial(n):
    if n < 0 or not isinstance(n, int):
        print("Your argument should be a positive integer")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))
print(factorial(-7))
print(factorial(6.3))