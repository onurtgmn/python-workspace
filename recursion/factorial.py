number = int (raw_input ("Enter a number : "))
def factorial (number):
    if (number == 1 or number == 0):
        return 1
    else :
        return number* factorial (number - 1)
print (factorial (number ))
