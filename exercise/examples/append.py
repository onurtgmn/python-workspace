def appendlist(element,lst):
    for i in lst:
        if (type(i)==list):
            i.append(element)
    return lst
print (appendlist("a",[[1,2],[2,3]]))
print (appendlist("a",[1,2,[3,4],["a","b"]]))
