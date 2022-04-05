class StringClass:

    def __init__(self):
        self.str1 = input("Enter String:- ")

    def lengthstring(self):
        return len(self.str1)

    def listcharacters(self, str2):
        return list(str2)


strclass = StringClass()
print(strclass.lengthstring())
print(strclass.listcharacters(str2="hello123"))


