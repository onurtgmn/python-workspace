while (True):
    element = int(raw_input ("Enter the element :"))
    print (element)
    decision = raw_input ("Do you want to continue ?(y/n)")
    if (decision == 'y'):
        continue ;
    elif (decision == 'n'):
        print ("Exiting program ...")
        break ;
    else :
        print ("Please enter only y or n ...")
            
    
