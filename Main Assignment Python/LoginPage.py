from UserPage import user


class login_Class:
    def __init__(self):
        self.adminID = "Admin"
        self.adminPass = "Admin@123"

    def Login_func(self):
        print()
        print("****** Welcome to BookMyShow ******")
        user_id = input("User: ")
        pswrd = input("Password: ")
        if user_id == self.adminID:
            if pswrd == self.adminPass:
                admin.adminLogin()
            else:
                print("Wrong Admin Password !!")
        else:
            user.userLogin(user_id, pswrd)


login = login_Class()

