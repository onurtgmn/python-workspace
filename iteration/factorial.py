print ("*****************")
print ("Factorial Computing Program")
print ("Please enter a number...")
print ("*****************")
number = int (raw_input ("Enter a number :"))
result=1
while (number > 0):
    result*=number
    number-=1
print (result)

