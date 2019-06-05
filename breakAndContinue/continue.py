print ("Without continue:")
for i in range (0,11):
    print (i)
print ("With continue:")
for i in range (0,11):
    if (i==5):
        continue
    print (i)

lst=[1,2,3,4,5]
print ("Continue in list:")
for i in range (0,len (lst)):
    if (i==2):
        continue
    print (lst[i])
