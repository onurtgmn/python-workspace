def checkAll(lst):
    for i in lst:
        if (bool(i)==False):
            return False
    return True
print (checkAll(["a",False]))
print (checkAll([1,0,3]))
print (checkAll([1,2]))
