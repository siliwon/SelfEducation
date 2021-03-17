n = int(input())
list = []
for i in range(1, n):
    list += [int(input())]

i = 1
for i in range(1, n + 1):
    if list.count(i):
        continue
    else:
        print(i)
