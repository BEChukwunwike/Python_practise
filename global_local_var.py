num = 9 # variable defined outside a function

def cube_num(num):
    #num = 5
    cube = num ** 3
    print(cube)

print(num) # prints num variable in the global scope
cube_num(num) #priorises num variable within the function(local variable)