list = list(map(int, input().split()))
new_list = []
for i in list:
    if new_list.count(i) == 0:
        new_list.append(i)
print(len(new_list))
