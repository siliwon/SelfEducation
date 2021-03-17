words = set()
with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        for word in line.split():
            words.add(word)
print(len(words))
