boy=float(raw_input("Lutfen boyunuzu giriniz:"))
kilo=float(raw_input("Lutfen kilonuuzu giriniz:"))
sonuc=kilo/(boy*boy)
print (sonuc)
if (sonuc<18.5):
    print ("Zayif")
elif (sonuc <25 ):
    print ("Normal")
elif (sonuc<30 ):
    print ("Fazla kilolu")
else :
    print ("Obez")
