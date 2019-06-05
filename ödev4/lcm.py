print ("***********************")
print ("LCM Computing Program...")
print ("Enter 2 number...")
print ("***********************")
first = int (raw_input ("Enter the first number :"))
second = int (raw_input ("Enter the second number:"))
def lcm (x,y):
    lcm = 1
    for i in range (1,x*y+1):
        if (i % x == 0 and i % y == 0):
            lcm = i
            break
    return lcm 
print ("LCM({},{}) = ".format(first,second)+str(lcm (first,second)))
            

    

