objects = [1, 2, 1, 3, 2, 4, 5, True, False, 0, 1]

unique = set()

for i in objects:
    unique.add(id(i))


print(len(unique))