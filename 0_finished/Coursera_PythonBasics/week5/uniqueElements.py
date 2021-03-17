list = list(map(int, input().split()))
new_list = []
for i in list:
    if list.count(i) == 1:
        new_list.append(i)
print(*new_list)
