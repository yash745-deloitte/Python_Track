class StringClass:

    def __init__(self):
        self.str1 = input("Enter String:- ")

    def length_string(self):
        return len(self.str1)

    def list_characters(self):
        return list(self.str1)


if __name__ == '__main__':

    strclass = StringClass()
    print(strclass.length_string())
    print(strclass.list_characters())


