dictionary = dict()
n = int(input())
for i in range(n):
    list = []
    for j in input().split():
        list.append(j)
    dictionary[list[0]] = list[1]
    list.clear()
word = input()

for key, value in dictionary.items():
    if key == word:
        print(value)
    elif value == word:
        print(key)
