print ("*********************")
print ("Buble Sort Algorithm...")
print ("*********************")
def bubbleSort(lst):
    swapped = True
    while (swapped):
        swapped = False 
        i = 0
        while (i<len (lst)-1):
            if (lst[i]>lst[i+1]):
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
                swapped = True 
            i+=1
    return lst
lst = [1,5,2,6,4]
print (bubbleSort(lst))

