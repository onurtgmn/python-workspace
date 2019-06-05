lst=[2,3,4.14,"Ankara"]
print ("Before changing")
print (lst)
lst[0]=0
print ("After changing")
print (lst)
print (len(lst))
print (lst[2])
print (lst[-1])
print (lst[1:3])
print (lst[:2])
print (lst[0:3:2])
print (lst[len(lst)-1])
print (lst[::-1])
lst2=["Kirikkale","Burdur",5,57.7]
print "liste 1 "+str(lst)
print "liste 2 "+str(lst2)
print "toplamlari "+str((lst+lst2))
print ("yeni liste 1")
lst=3*lst
print (lst)
lst[:2]=[10,11]
print (lst)
lst.append(7)
lst.append("Ankara ankara guzel Ankara")
print (lst)
lst=[1,2,3,4,5]
print ("yeni liste :"+ str (lst))
lst.append(3.14) 
lst.append(6)
print (lst)
lst=[1,2,3,4,5]
lst.append([1,2,3])
print (lst)
lst=[1,2,3,4,5]
lst.pop()
print (lst)
lst.pop(1)
print (lst)
lst.pop()
print (lst)#Append ,pop,sort ve reverse metodu (listelerle ilgili)
lst=[1,4,2,8,5]
lst.sort()
lst.reverse()
print (lst)
lst=["Ankara","Adiyaman","Zonguldak","Balikesir"]
lst.sort()
print (lst)
lst=[[1,2],[3,4],[5,6]]
print (len (lst))
print (lst[0][1])
