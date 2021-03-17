list = list(map(int, input().split()))
counter = 0
for i in list:
    if list.count(i) > list.count(counter):
        counter = i

print(counter)
