#This function takes a list and return the index of first number in it. if not found, returns -1.
def find_the_first_number (lst):
    i=0
    index = -1
    while (i<len(lst)):
        if (type(lst[i])==int or type(lst[i])==float):
            index = i
            break
        i+=1
    return index
print (find_the_first_number(["a","Onur","*",9,7.6]))
