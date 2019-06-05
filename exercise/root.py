#2.derece den denklem koku bulma 
a=int (raw_input ("a:"))
b=int (raw_input("b:"))
c=int (raw_input ("c:"))
delta=b*b-4*a*c
root1=(-b+delta**0.5)/2*a
root2=(-b-delta**0.5)/2*a
print ("First root:"+str(root1))
print ("Second root:"+str(root2))
