print ("*******************")
print ("Finding all of the divider of a number ...")
print ("To quit program ,please press q...")
print ("*******************")
lst = []
def findDivider (number):
    for i in range (1,number+1):
        if (number % i == 0):
            lst.append (i)
    return lst
while (True):
    lst = []
    number = raw_input ("Enter the number :")
    if (number == "q"):
        print ("Exiting program ...")
        break
    number = int (number)
    print (findDivider(number))


