been_called = False
def example2():
    been_called = True
    return been_called
print(example2())
print(been_called)

count = 0
def example3():
    global count
    count = count + 1
    return count
    
print(example3())
print(count)

known = {0:0, 1:1}
def example4():
    known[2] = 1
    return known
print(example4())
print(known)