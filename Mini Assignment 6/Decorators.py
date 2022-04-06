def deco(func):
    def inner(a, b):
        return func(a, b)

    return inner


@deco
def multiply(num1, num2):
    print(num1 * num2)


multiply(5, 5)
multiply(5, 5)
