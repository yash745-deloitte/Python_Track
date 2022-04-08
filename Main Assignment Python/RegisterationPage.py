import openpyxl


class Register_Class:
    def Register_func(self):
        print()
        print("***** Create New Account *****")
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        age = input("Age: ")
        password = input("Password: ")
        user_book = openpyxl.load_workbook()


register = Register_Class()

