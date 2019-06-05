length = int (raw_input ("Enter the length:"))
def formList(length):
    i=0
    lst = []
    while(i<length):
        element = raw_input ("Enter the element:")
        lst.append(element)
        i+=1
    return lst
def checkList(formList(length)):
    for element in lst:
        if (bool(element)==False ):
            result = False 
            break 
        else :
            result = True
    return result
print (checkList(lst))


    

