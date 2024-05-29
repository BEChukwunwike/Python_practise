def is_palindrome():
    # Ask the user to input the text
    text = input("Enter the text to check for palindrome: ")

    # Preprocess the text: remove punctuation and spaces, convert to lowercase
    processed_text = "".join(char.lower() for char in text if char.isalnum())
    print ("Processed text: ", processed_text)

    if processed_text == "":  # checks if the processed text is empty
       print("enter some valid text")
       return False

    else:
        # Check if the processed text is equal to its reverse
        is_palindrome = processed_text == processed_text[::-1]
        if is_palindrome:
            print("The text is a palindrome.")
        else:
            print("The text is not a palindrome.")
        print (is_palindrome)
        return is_palindrome

is_palindrome()
