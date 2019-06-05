print ("**********************")
print ("Great Number Between 1 and 1000...")
print ("**********************")
#Great Number :6 = 1+2+3(Not including itself)
def summing(number):
    result = 0 
    for i in range (1,number):
        if (number % i == 0):
            result += i
    return result
def findGreatNumber():
    lst = []
    for i in range (1,1001):
        if (i == summing(i)):
            lst.append (i)
    return lst
print (findGreatNumber())





