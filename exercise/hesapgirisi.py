i=0
while (i<3):
    username="tgmn06"
    password="123456789"
    n=raw_input ("Enter your user name :")
    p=raw_input ("Enter your password:")
    if (username==n and password==p):
        print ("You wiil enter the system...")
        break
    elif (username==n and password!=p):
        i+=1    
        print ("Please enter correct password...")
    elif (username !=n and password==p):
        i+=1
        print ("Please enter correct username...")
    else:
        i+=1
        print ("Username and password are incorrect...")
if (i==3):
    print ("You have entered wrong data 3 times...")
