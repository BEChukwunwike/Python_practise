try:
    # Trying to open a non-existent file.
    with open('sample_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError as e:
    # Handle the error
    print(f"Error: {e}")