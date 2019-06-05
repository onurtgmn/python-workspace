print ("********************")
print ("GCD Computing Program ...")
print ("********************")
lst= []
first = int (raw_input ("Enter the first number:"))
second = int (raw_input ("Enter the second number:"))
def findDivider(number):
    lst = []
    for i in range (1,number+1):
        if (number % i == 0):
            lst.append (i)
    return lst
def gcd (x,y):
    lst2 = findDivider(x)
    lst3 = findDivider(y)
    lst4 = []
    for j in lst2:
        for k in lst3:
            if (j == k):
                lst4.append(j)
    return lst4[len(lst4)-1]
print gcd (first,second)
    
    
                



