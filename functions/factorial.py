number = int (raw_input ("Number :")) 
def factorial (number):
    result = 1
    while (number > 0 ):
        result*=number 
        number -= 1
    return result
print (factorial (number))


