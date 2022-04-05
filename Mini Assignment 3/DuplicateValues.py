listoflist = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]

for list_element in listoflist:
    dict = {}
    for element in list_element:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1

    for element in dict:
        if dict[element] > 1:
            print(element," -> ", dict[element])