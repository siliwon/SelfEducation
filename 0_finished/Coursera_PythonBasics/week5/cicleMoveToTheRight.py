list = list(map(int, input().split()))
new_list = []
new_list.append(list[-1])
list.pop(-1)
for i in list:
    new_list.append(i)
print(*new_list)
