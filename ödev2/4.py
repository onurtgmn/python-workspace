def mutlakAl(sayi):
    if (sayi<0):
         return -sayi
    else :
         return sayi
answer=raw_input ("Hangi seklin tipini ogrenmek istiyorsunuz?")
if (answer=="Dortgen"):
    a=int (raw_input ("Ilk kenar:"))
    b=int (raw_input ("Ikinci kenar:"))
    c=int (raw_input ("Ucuncu kenar:"))
    d=int (raw_input ("Son kenar:"))
    if(a==b and b==c and c==d ):
        print ("Dortgen bir karedir...")
    elif ((a==b and c==d) or(a==c and b==d) ):
        print ("Dortgen bir dikdortgendir...")
elif(answer=="Ucgen"):
    a=int (raw_input("Ilk kenar:"))
    b=int (raw_input("Ikinci kenar:"))
    c=int (raw_input("Ucuncu kenar:"))
    if (mutlakAl(a-b)<c<a+b and mutlakAl(a-c)< b<a+c and mutlakAl(b-c)<a<b+c):
        if (a==b and b==c ):
            print ("Ucgen eskenar ucgendir...")
        elif (a==b or a==c or b==c ):
            print ("Ucgen ikizkenar ucgendir...")
        else :
            print ("Ucgen cesitkenar ucgendir...")
    else :
        print ("Ucgen belirtmez...")
else :
     print ("Lutfen sadece Ucgen yada Dortgen yaziniz...")
