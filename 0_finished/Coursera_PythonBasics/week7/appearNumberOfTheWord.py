dictionary = dict()
with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        for i in line.split():
            if i not in dictionary.keys():
                print(0, end=' ')
                dictionary[i] = dictionary.get(i, 1)
            else:
                print(dictionary[i], end=' ')
                dictionary[i] += 1
