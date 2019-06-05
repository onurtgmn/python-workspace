tek=[]
cift =[]
lst=[1,2,3,4,5,6,7]
for i in lst :
    if (i%2==0):
        cift.append(i)
    else:
        tek.append(i)
print ("Tekler:"+str(tek))
print ("Ciftler:"+str(cift))
print ("tek sayilar")
for i in tek :
    print i
print ("Cift sayilar")
for j in cift :
    print j
        
