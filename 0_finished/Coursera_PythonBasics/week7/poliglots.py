pupils = int(input())
languages = dict()
for i in range(pupils):
    amount = int(input())
    for j in range(amount):
        language = input()
        languages[language] = languages.get(language, 0) + 1

first_list = []
for key, value in languages.items():
    if value == pupils:
        first_list.append(key)
print(len(first_list), *first_list, sep='\n')
second_list = []
for key, value in languages.items():
    second_list.append(key)
print(len(second_list), *second_list, sep='\n')
