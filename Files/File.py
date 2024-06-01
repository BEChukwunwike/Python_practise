# Read a File
with open(r'c:\Users\user\Downloads\Python_practise\Files\sample.txt', 'r', encoding= 'utf-8') as file:
    print(file.read())
    
# Write to a File
with open(r'c:\Users\user\Downloads\Python_practise\Files\output.txt', 'w', encoding= 'utf-8') as file:
    file.write('Yaay! I successfully used the write mode. the file name provided was not existent so It created a new file')