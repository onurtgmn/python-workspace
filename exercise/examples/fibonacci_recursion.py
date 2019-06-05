print ("fibonacci sequence : 1 1 2 3 5 ...")
number = int (raw_input ("Enter the number:"))
def fibonacci (number):
    if (number == 1 or number == 2):
        return 1 
    else :
        return fibonacci(number-1)+fibonacci (number-2)
print (fibonacci (number))
