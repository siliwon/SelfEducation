list = list(map(int, input().split()))
new_list = []
for i in list:
    if i % 2 == 1:
        new_list.append(i)
print(min(new_list))
