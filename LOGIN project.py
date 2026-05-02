import random
password="python lub"
while True:
    tries=0
    while tries<3:
        user_password=input("Enter your password: ")
        if(user_password==password):
            print("acess guarenteed")
            print("THANK YOU FOR LOGIN. YOUR LOGIN WAS SUCCESSFUL")
            exit()
        else:
            tries+=1
            print("acess denied")
    if(tries==3):
        print("SORRY :(, Your account has been locked")
        choice=input("Do you want to change the password(y/n): ")
        if(choice=="yes"):
            gmail=input("enter your gmail: ")
            gpassword=input("enter your gmail password: ")
            print("We have sent an OTP to ur gmail")
            OTP=random.randint(999,10000)
            print("your OTP is ",OTP)
            user_OTP=int(input("Please enter your OTP"))
            if(user_OTP==OTP):
                print("OTP verification successful")
                new_pass=input("enter your new password: ")
                password=new_pass
                print("yor password has been reseted")
                print("your current new password is: ",password)
            else:
                print("INVALID OTP... Please enter the correct OTP to reset your password")
        else:
            print("TRY AGAIN... After 30 minutes")
            exit()
