print ("Fibonacci sequences 1 1 2 3 5 8 ...")
"""
a = 1       b = 1
a = 1       b = 2 (a+b)
a = 2       b = 3 (a+b)



"""
term_number = int (raw_input ("Enter the term number :"))
def fibonacci (term_number):
    a = 1
    b = 1
    i = 2
    while(i<term_number):
        temp = b
        b = a+b
        a= temp
        i+=1
    return b
print (fibonacci (term_number))
