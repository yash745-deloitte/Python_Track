class Calculator(Exception):
    pass


while True:
    formula = input("Enter the formula to calculate: ")
    if formula == "quit":
        break
    else:
        lst = formula.split(" ")
        while True:
            try:
                if len(lst) != 3:
                    raise Calculator
                else:
                    if lst[1] == '+' or lst[1] == '-':
                        try:
                            a = int(lst[0])
                            b = int(lst[2])
                            if lst[1] == '+':
                                print(a + b)
                                break
                            else:
                                print(a - b)
                                break
                        except Calculator:
                            print("Formula is invalid")
                            break
                    else:
                        raise Calculator
            except Calculator:
                print("Formula is Invalid")
                break
