lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
a = 0
A = 0

countit = lambda i, ch: i.count(ch)
lstmap = list(map(list, lst1))
for char in lstmap:
    A += countit(char, 'A')
    a += countit(char, 'a')

print(A, a)