def nested_sum (lst):
    summation = 0
    for i in lst :
        if (type (i) == list):
            for j in i:
                summation += j
        else :
            summation += i
    return summation 
print (nested_sum([1,2,3,4]))
print (nested_sum([[1,2],3,4]))

