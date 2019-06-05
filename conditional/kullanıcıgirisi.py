#Kullanici girisi kullanici adi ve parola ya gore olacak.
#Eger kullanici adi ve sifre dogru olursa giris yapilacak.
#kullanici adini tgmn06 ve sifreyi Onur123 olarak al.
username="tgmn06"
password="Onur123"
user_name=raw_input ("Enter your user name :")
user_password=raw_input ("Enter your password:")
if (user_name==username and user_password==password):
    print ("Welcome to our system ...")
elif (user_name!=username and user_password ==password):
    print("Please enter correct username...")
elif (user_name==username and user_password!=password):
    print ("Please enter correct password...")
else :
    print ("You should correct both of them ...")

