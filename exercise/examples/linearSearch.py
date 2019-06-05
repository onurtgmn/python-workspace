def linearSearch (element,lst):
    key = True
    for i in lst :
        if (element != i):
           key = False 
        else:
            key = True 
    return key
print (linearSearch ("a",[1,2,3,"a"]))
print ("*******************************")
print (linearSearch ("w",["a","b","c"]))
