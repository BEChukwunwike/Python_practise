# Read a File
with open(r'c:\Users\user\Downloads\Python_practise\Files\sample.txt', 'r', encoding= 'utf-8') as file:
    print(file.read())
    
# Write to a File
with open(r'c:\Users\user\Downloads\Python_practise\Files\output.txt', 'w', encoding= 'utf-8') as file:
    file.write('Yaay! I successfully used the write mode.\nThe file name provided was not existent so It created a new file')
    
# Append to a File
with open(r'c:\Users\user\Downloads\Python_practise\Files\output.txt', 'a', encoding= 'utf-8') as file:
    file.write('\nWell, see who just used the append mode. Yippy!')
    
# Read a File Line by Line
with open(r'c:\Users\user\Downloads\Python_practise\Files\output.txt', 'r', encoding= 'utf-8') as file:
    for line in file:
        print(line, end='')
        
# Copy File.
with open(r'c:\Users\user\Downloads\Python_practise\Files\output.txt', 'r', encoding='utf-8') as file:
    with open(r'c:\Users\user\Downloads\Python_practise\Files\copy.txt', 'w', encoding= 'utf-8') as file2:
        for line in file:
            file2.write(line)

# Count words in a file
with open(r'c:\Users\user\Downloads\Python_practise\Files\output.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    words = text.split()
    word_count = len(words)
    print(f'\nWord count for output.txt: {word_count}')
    
# Find and replace
with open(r'c:\Users\user\Downloads\Python_practise\Files\sample.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    text = text.replace('This is', 'I created')
    print(text)
    with open(r'c:\Users\user\Downloads\Python_practise\Files\modify_sample.txt', 'w', encoding='utf-8') as file:
        file.write(text)
        
# Merge Files
with open(r'c:\Users\user\Downloads\Python_practise\Files\modify_sample.txt', 'r', encoding='utf-8') as file:
    file = file.read()
    with open(r'c:\Users\user\Downloads\Python_practise\Files\output.txt', 'r', encoding='utf-8') as file1:
        file1 = file1.read()
        merged_files = file + '\n' + file1
        with open(r'c:\Users\user\Downloads\Python_practise\Files\merged.txt', 'w', encoding='utf-8') as file2:
            file2.write(merged_files)

import os
os.remove(r'c:\Users\user\Downloads\Python_practise\Files\copy.txt')