size = int(input("Enter the number:- "))
arr = [1]
for i in range(size - 1):
    arr.append(0)

for i in arr:
    print(i, end=" ")

print()
for i in range(1, size, 1):
    for j in range(i, 0, -1):
        arr[j] = int(arr[j]) + int(arr[j - 1])
    for e in arr:
        print(e, end=" ")
    print()

