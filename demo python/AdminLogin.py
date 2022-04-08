class AdminLogin_Class:
    def AdminLogin_func(self):
        print("******Welcome Admin*******")
        print("1. Add New Movie Info ")
        print("2. Edit Movie Info ")
        print("3. Delete Movies ")
        print("4.Logout ")
        ch = int(input("Enter: "))
        if ch == 1:
            # addnew
        elif ch == 2:
            # edit
        elif ch == 3:
             # delete
        elif ch == 4:
             # logout
        else:
            print("Invalid Input !!")

admin = AdminLogin_Class()