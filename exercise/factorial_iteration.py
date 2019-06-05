print ("""******************

Faktorial computing program 

To quit,please enter q...

*******************""")
#Prompt one number from the user .If user press q ,quit the program . We expect program to run until user press q ...

while (True):
    carpim=1
    sayi=raw_input ("Please enter a number:")
    if (sayi=="q"):
        print ("Exiting program...")
        break
    else :
        sayi=int (sayi)
        while (sayi>0):
            carpim*=sayi
            sayi-=1
    print ("Factorial : "+ str (carpim) )

    
