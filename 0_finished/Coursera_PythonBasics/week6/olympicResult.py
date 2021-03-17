n = int(input())
list = []
for i in range(n):
    list.append(input().split())

list.sort(key=lambda x: (-int(x[1]), x[0]))
for i in list:
    print(i[0])
