print ("Before break")
for i in range (0,11):
    print (i)
print ("After break")
for i in range (0,11):
    if (i==5):
        break
    print (i)
lst =[1,2,3,4,5]
print ("The list before break")
for i in range (0,len (lst)):
    print (lst[i])
print ("the list after break")
for i in range (0,len(lst)):
    if (i==2):
        break 
    print (lst[i])

