f = open("a.txt", "r")
words = f.read().split()

max = 0
longest = ""
for x in words:
    if len(x) >= max:
        max = len(x)
        longest = x

print(longest)
