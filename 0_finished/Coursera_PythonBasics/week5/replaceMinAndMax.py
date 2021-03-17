list = list(map(int, input().split()))
minimum = min(list)
minimum_index = list.index(minimum)
maximum = max(list)
maximum_index = list.index(maximum)
new_list = []
for i in list:
    if i == minimum:
        new_list.append(maximum)
    elif i == maximum:
        new_list.append(minimum)
    else:
        new_list.append(i)
print(*new_list)
