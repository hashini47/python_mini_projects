pin=1234
user_pin=int(input("enter ur pin: "))
user_balance=1000
print("------------------MY_ATM MENU----------------")
while True:
    print("1. View balance")
    print("2. Credit Amount")
    print("3. withdraw Amount")
    print("4. Exit")
    break
print("---------------------------------------------")
if(user_pin==pin):
    print("WELCOME TO MY ATM....")
    while True:
        choice=input("enter ur choice(1-2-3-4): ")
        if(choice=="1"):
            print("Your balance: ",user_balance)
        elif(choice=="2"):
            amount=int(input("Enter the amount to be credited: "))
            print("your amount was deposited successfully.....!!")
            user_balance+=amount
           
            view_balance=int(input("enter 69 to view balance: "))
            if(view_balance==69):
                print("Your current balance after credit is: ",user_balance)
            else:
                break
        elif(choice=="3"):
            amount=int(input("enter amount to withdraw:"))
            if(amount<=user_balance):
                print("your amount was successfully withdraw")
                user_balance-=amount
                view_balance=input("enter ur key to view balance:")
                if(view_balance=="69"):
                    print("Your current balance after deposit is: ",user_balance)
                else:
                    break
        elif(choice=="4"):
            print("Thank you for using my ATM. Have a good day")
            break
else:
    print("Sorry u have entered a wrong pin. Please enter a correct pin. Thank you :)")
