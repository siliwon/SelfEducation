list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list = []
list.extend(list_a)
list.extend(list_b)
list.sort()
print(*list)
