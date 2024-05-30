def display_name():
    name = input("Enter your name: ")
    n = int(input("Enter the number of character(s) to display: "))
    print("The first", n, "characters from your name are '", name[:n], "'")
    return name[:n]

display_name()

def count_vowel():
    count = 0
    name = input("Enter your name: ")
    vowels = "aeiouAEIOU"
    for c in name:
        if c in vowels:
            count += 1
    print("There are", count, "vowels in", name)
    return count
count_vowel()

def reverse_name():
    name = input("Enter your name: ")
    reversed_name = name[::-1]
    print("Your name was successfully reversed \n", reversed_name)

reverse_name()

while True:

    while 1 > 0:

        break

    print("Got it!")

    break