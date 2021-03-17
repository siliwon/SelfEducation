step = int(input())
list = list(map(int, input().split()))
list.sort()
i = 0
counter = 0
while i < len(list):
    if list[i] < step:
        i += 1
    elif step <= list[i]:
        counter += 1
        step = list[i] + 3
        i += 1
print(counter)
