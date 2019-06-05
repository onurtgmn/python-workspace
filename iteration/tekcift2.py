lst=[1,2,3,4,5,6,7,8]
tek=[]
cift=[]
i=0
while (i<len (lst)):
    if (lst[i]%2==0):
        cift .append(lst[i])
    else:
        tek.append(lst[i])
    i+=1
print ("Tekler:"+str(tek))
print ("Ciftler:"+str(cift))
        
