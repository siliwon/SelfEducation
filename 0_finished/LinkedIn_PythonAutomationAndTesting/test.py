 = 'aaaaabbbccddddddddddeeeff'


b = list()
for i in a:
    if i not in b:
        b.append(i)
print(''.join(b))
