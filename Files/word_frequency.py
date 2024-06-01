import string

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

myFile = read_file(r'C:\Users\user\Downloads\Python_practise\Files\a_LittleMaid.txt')

clean = clean_text(myFile)
print(clean[:1000])

def word_counts(clean):
    words = clean.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

word_count = word_counts(clean)
print(word_count)
