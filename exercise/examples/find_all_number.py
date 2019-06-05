print("**************************")
print("Finding the indices of all number ...")
print("**************************")
def find_all_number(lst):
    i=0
    result = []
    while (i<len(lst)):
        if (type(lst[i])== int or type(lst[i])==float):
            result.append(i)
        i+=1
    return result 
print ("The indices are :"+str(find_all_number(["a","b",9,"8",7])))
            
