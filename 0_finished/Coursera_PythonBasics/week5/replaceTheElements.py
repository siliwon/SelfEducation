list = list(map(int, input().split()))
new_list = []
for i in range(len(list) - 1, -1, -1):
    new_list.append(list[i])
print(*new_list)
