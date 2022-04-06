lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]


filtered_positive_numbers = list([-x for x in (filter(lambda x: x < 0, lst1))])
print(filtered_positive_numbers)
