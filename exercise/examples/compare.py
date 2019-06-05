print ("***************************")
print ("Comparing two floating point number by using 0.000001")
print ("***************************")
a = float (raw_input("Enter the first number:"))
b = float (raw_input ("Enter the second number:"))
def absolute (value):
    if (value<0):
        value = -value
    return value
def checkEqual(a,b):
    result = True
    if (absolute(a-b) > 0.000001):
        result = False
    return result
print (checkEqual(a,b))
