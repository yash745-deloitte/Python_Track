Dict1 = {"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}

list1 = []

for element in Dict1:
    list2 = []
    list2.append(element)
    for ele in Dict1[element]:
        list2.append(ele)
    list1.append(list2)

print(list1)