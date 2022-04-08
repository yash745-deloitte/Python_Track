from RegisterationPage import register
from LoginPage import login


class HomePage_Class:
    def Homepage_func(self):
        while True:
            print("****** Welcome to BookMyShow ******")
            print("1. Login")
            print("2. Register new account")
            print("3. Exit")
            ch = int(input("Enter: "))
            if ch == 1:
                login.LoginPage_func()
            elif ch == 2:
                register.Register_func()
            elif ch == 3:
                quit(0)
            else:
                print("Invalid Input !!")


if __name__ == '__main__':
    home = HomePage_Class()
    home.Homepage_func()
