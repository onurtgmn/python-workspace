print ("******************")
print ("Fibonacci Computing program ...")
print ("Please enter the fibonacci term that you want to compute... ")
print ("******************")
number = int (raw_input ("Enter a number:"))
def fibonacci(number):
    if (number==1 or number ==2 ):
        return 1
    else :
        return (fibonacci(number-1)+fibonacci(number-2))
print ("The {}. term in fibonacci sequences is {}...".format (number,fibonacci(number)))
