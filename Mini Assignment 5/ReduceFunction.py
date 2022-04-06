from operator import add
from operator import mul
from functools import reduce

lst1 = [1, 2, 3, 4, 5, 6]
ans2 = reduce(mul, lst1)
print(ans2)
