n = 5
for i in range(n):
    for j in range(n):
        if i == j or i == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
