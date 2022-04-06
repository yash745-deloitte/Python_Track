def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a, b = b, a + b


num1 = int(input("Enter value of length of fib series:- "))
for x in fib(num1):
    print(x)
