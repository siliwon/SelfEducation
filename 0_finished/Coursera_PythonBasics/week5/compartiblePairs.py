list = list(map(int, input().split()))
counter = 0
for i in range(0, len(list)):
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            counter += 1

print(counter)
