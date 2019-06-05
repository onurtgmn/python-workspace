print ("**********************")
print ("Finding Armstrong Number :")
print ("Enter your number to understand whether it is armstrong number ...")
print ("**********************")
number = int (raw_input ("Enter the number:"))
temp = number
temp2 = number
digit = 0
summation = 0 
while (number > 0 ):
    number/=10
    digit+=1
print ("Digit:"+str(digit))
while (temp > 0 ):
    remainder = temp % 10 
    summation += remainder ** digit
    temp/= 10 
print ("Summation :"+ str (summation))
if (temp2 == summation ):
    print ("This number is an armstrong number ...")
else :
    print ("This is not an armstrong number ...")


