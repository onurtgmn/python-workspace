print ("3 'e bolunen sayilarin bastirilmasi")
lst=[]
for i in range (1,100):
    if (i % 3 != 0):
        continue 
    lst.append(i)
print (lst)

