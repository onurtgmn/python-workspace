def isPrime (number):
    for i in range (2,number):
        if (number % i == 0):
            return False
    return True
def find_divider (x):
    lst = []
    i=1
    while (i<=x):
        if (x % i == 0 and ):
            lst.append(i)
        i+=1
    return lst
def factorial_how_many(factorial,divider):
    i = 1
    count = 0 
    while (i<=factorial):
        for j in find_divider(i):
            if (j==divider):
                count+=1
        i+=1
    return count
print (factorial_how_many(25,3))


