islem =None
while (islem!="S"):
    a=int (raw_input("Lutfen ilk sayiyi giriniz:"))
    b=int (raw_input ("Lutfen ikinci sayiyi giriniz:"))
    islem=raw_input("Lutfen yapmak istediginiz islemi giriniz:")
    if (islem=="+"):
        print (a+b)
        
    elif (islem =="-"):
        print (a-b)
    
    elif (islem =="*"):
        print (a*b)
        
    elif (islem =="/"):
        print (float(a)/b)
    
    else :
        print ("Lutfen gecerli bir karakter giriniz.")

