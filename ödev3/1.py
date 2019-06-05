number = int (raw_input ("Enter a number:"))
result = 0
for i in range (1,number):
    if (number % i == 0 ):
        result+=i
if (number == result):
    print ("Great number...")
else :
    print ("Not a great number ...")

