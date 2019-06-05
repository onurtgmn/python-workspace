#fibonacci serisi 1 1 2 3 5 8 13 .....
print ("""**************************

Computing fibonacci sequences

The first 20 terms in fibonacci

**************************""")

a=1
b=1
fibonacci=[a,b]
i=0
while (i<18):
    temp=a
    a=b
    b=temp+b
    i+=1
    fibonacci.append (b)
print (fibonacci)
print ("Length of list:"+str (len (fibonacci)))
sayi=int (raw_input ("Enter the number to find fibonacci terms:"))
print ("The term that you entered in fibonacci :"+str (fibonacci[sayi-1]))
