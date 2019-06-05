number = int (raw_input ("Enter the number :"))
summation = 0
for i in range (1,number):
    if (number%i==0):
        summation += i
if (summation==number):
    print ("{} is perfect number...".format(number))
else :
    print ("{} is not a perfect number...".format(number))
        
