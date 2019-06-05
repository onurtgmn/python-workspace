print ("""*************************

Welcome to atm machine program

1.Ask your account

2.Cash deposit

3.Withdraw money

To quit program ,enter q ...

*************************""")
money = 1000
while (True):
    op=raw_input ("Enter the operation number that you want to do :")
    if (op=="q"):
        print ("Exiting program...")
        break
    elif (op=="1"):
        print (money)
    elif (op=="2"):
        cash = int (raw_input ("Enter the cash that you want to deposit:"))
        money+=cash
        print ("Total money :"+str (money))
    elif (op=="3"):
        cash = int (raw_input ("Enter the cash that you want to withdraw:"))
        if (cash > money):
            print ("You can't withdraw more than money that you have...")
        else:
            money-=cash 
            print ("Total money :"+str (money))
    lst=["1","2","3"]
    if (op in lst):
        more = raw_input ("Do you want to do more operation?(y or n):")
        if (more=="y"):
            continue
        else :
            print ("Exiting program...")
            break
    else :
        print ("Please enter a valid integer(only 1 ,2 or 3...)")

