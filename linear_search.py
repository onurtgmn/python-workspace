lst = [1,2,3,4,5,6]
def find_index_of_element (element,lst):
    i = 0 
    index = 0
    while (i < len (lst)):
        if (element == lst[i]):
            index = i
        i+=1
    return index
print (find_index_of_element(3,lst))

