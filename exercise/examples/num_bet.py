# this function takes two integers and generates an ordered list of the numbers in between them
lst = []
def number_between(x,y):
    for i in range (x+1,y):
        lst.append(i)
    return lst
print (number_between(3,10))
