print ("***************************")
print ("Absolute value program...")
print ("To quit program,please press q... ")
print ("***************************")
def absolute (value):
    if (value >= 0):
        return value
    return -value
while (True):
    value =raw_input ("Enter the number:")
    if (value=="q"):
        print ("Exiting program")
        break
    value = int (value)
    print (absolute(value))
