def oneCaps(word):
    result = 0
    for c in word:
        result += int(c.isupper())
    return result == 1


with open('input.txt', 'r', encoding='utf-8') as inf:
    words = set()
    n = int(inf.readline())
    for _ in range(n):
        words.add(inf.readline().strip())
    text = inf.read().split()
lowwords = {s.lower() for s in words}
err = 0
for word in text:
    if word not in words:
        if word.lower() in lowwords:
            err += 1
        elif word.islower():
            err += 1
        elif not oneCaps(word):
            err += 1
print(err)
