words = dict()
with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        for word in line.split():
            if word not in words.keys():
                words[word] = 1
            else:
                words[word] += 1

often_word = max(words.values())
final_list = []
for key, value in words.items():
    if value == often_word:
        final_list.append(key)
print(min(final_list))
