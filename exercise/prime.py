print ("********************")
print ("Is Prime Or Not?")
print ("To quit program , please press q ...")
print ("********************")
def IsPrime (number ):
    for i in range (2,number):
        if (number % i == 0 ):
            return 0
    return 1
while (True):
    number = raw_input ("Enter the number :")
    if (number == "q"):
        print ("Exiting program...")
        break 
    number = int (number)
    if (number== 1 or number == 0):
        print ("{} is not a prime number...".format(number))
    elif (IsPrime (number) == 1):
        print ("{} is a prime number...".format(number))
    else :
        print ("{} is not a prime number...".format(number))
