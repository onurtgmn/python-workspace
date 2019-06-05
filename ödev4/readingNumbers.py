print ("************************")
print ("Number Raeding System...")
print ("Please enter a two digit number ...")
print ("To quit program,please enter q:")
print ("************************")
def reading (number):
    one = ["Bir","Iki","Uc","Dort","Bes","Alti","Yedi","Sekiz","Dokuz"]
    ten = ["On ","Yirmi ","Otuz ","Kirk ","Elli ","Atmis ","Yetmis ","Seksen ","Doksan "]
    digit1 = number % 10 
    digit2 = int (number / 10) 
    return (ten [digit2 -1] + one [digit1 -1])
while (True):
    number = raw_input ("Enter the number:")
    if (number == "q"):
        print ("Exiting Program...")
        break 
    number = int (number)
    print (reading(number))
