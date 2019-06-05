lst = []
for i in range (1,101):
    if (i % 2 == 0):
        lst.append (i)
print ("Liste"+str(lst))
sayi = int (raw_input ("Sayi:"))
print ("Sayi. eleman : "+str (lst[sayi-1]))
