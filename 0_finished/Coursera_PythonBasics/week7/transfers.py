a1, b1, a2, b2 = map(int, input().split())

first_stops = set()
second_stops = set()

for i in range(min(a1, b1), max(a1, b1) + 1):
    first_stops.add(i)
for i in range(min(a2, b2), max(a2, b2) + 1):
    second_stops.add(i)
list = first_stops.intersection(second_stops)
print(len(list))
