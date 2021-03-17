elections = dict()
with open('input.txt', 'r', encoding='utf8') as file:
    for line in file:
        line = line.strip()
        name, vote = line.split()
        if name not in elections.keys():
            elections[name] = int(vote)
        else:
            elections[name] += int(vote)

for key, value in sorted(elections.items(), key=lambda x: (x[0], x[1])):
    print(key, value)
