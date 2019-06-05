print ("********************")
print ("Summation Of Number In Loop")
print ("Press q to quit")
print ("********************")
toplam = 0
while (True):
    sayi = raw_input ("sayi:")
    if (sayi=="q"):
        print ("Exiting program...")
        break 
    sayi = int (sayi)
    toplam+=sayi 
print ("Toplam : "+str (toplam))
