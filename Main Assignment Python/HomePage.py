import RegisterationPage import Register


class HomePage_Class:
    def homepage_func(self):
        while True:
            print("****** Welcome to BookMyShow ******")
            print("1. Login")
            print("2. Register new account")
            print("3. Exit")
            ch = int(input("Enter: "))
            if ch == 1:


            elif ch == 2:
                RegisterationPage.Register