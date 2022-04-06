from operator import add
from operator import mul
from functools import reduce

lst1 = [1, 2, 3, 4, 5, 6]
ans1 = reduce(add, lst1)
lst2 = [ans1, 2, 2]
ans2 = reduce(mul, lst2)
print(ans2)
