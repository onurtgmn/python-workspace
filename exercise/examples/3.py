def find_how_many (factorial , divider):
    lst = []
    summation = 0 
    while (factorial >= divider):
        factorial = int (factorial/divider)
        summation+= factorial
        
    return summation
print (find_how_many(31,3))
        

