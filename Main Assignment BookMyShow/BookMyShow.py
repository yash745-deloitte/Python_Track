from Login import *

class Homepage:
    def homeinfo(self):
        print("*****Welcome To Book My Show****")
        print("1. Login")
        print("2. Register a new account")
        print("3. Exit")
        print(" ")
        a = int(input("Enter Your Choice: "))
        if a == 1:
            loginObj = Login()
            loginObj.log()
        elif a == 2:
            registerObj = Register()
            registerObj.newuser()
        elif a == 3:
            print("Bye Bye!")
            exit()
        else:
            print("Invalid Input")


while True:
    obj1 = Homepage()
    obj1.homeinfo()
    del obj1