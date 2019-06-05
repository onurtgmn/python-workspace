def sum_all(lst):
    if (len(lst)==1):
        return lst[0]
    elif (type (lst[0])==list):
        return sum_all(lst[0])+sum_all(lst[1:])
    else :
        return lst[0]+sum_all(lst[1:])
lst =[1,2,3]
lst2=[[1,2],3,4]
print (sum_all(lst))
print (sum_all(lst2))
print(sum_all([5]))
