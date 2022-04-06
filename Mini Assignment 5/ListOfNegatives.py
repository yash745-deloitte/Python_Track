lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]


filtered_positive_numbers = list(filter(lambda x: True if x > 0 else False, map(lambda x: x * -1, lst1)))
print(filtered_positive_numbers)

