import string

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

myFile = read_file('./a_LittleMaid.txt')

clean = clean_text(myFile)
print(clean[:1000])