print ("*********************")
print ("The fibonacci program ...")
print ("Please enter the term number that you want to learn...")
print ("*********************")
first = 1
other = 1
number = int (raw_input ("Enter the number :"))
a=number
number-=2
while(number > 0 ):
    temp = first
    first = other 
    other = temp + other 
    number -=1
print ("The {}. term in fibonacci is {}".format (a,other))

