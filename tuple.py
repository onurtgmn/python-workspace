#count ve index metodlari
#in strings and also tuples, they don't support item assignment.However,lists support item assignment.You can change the index in ONLY lists. 
tup=(1,2,3,4,5,"Ankara","Zonguldak")
print (type(tup))
print (tup[1])
print (tup[-1])
print (tup[:2])
print (tup[::-1])
tup2=(1,1,2,2,2,4,4,4,4)
print (tup2.count(2))
print (tup2.count(0))
print (tup2.count(1))
print (tup2.index(2))
print (tup.index (5))
print (tup.index("Ankara"))

