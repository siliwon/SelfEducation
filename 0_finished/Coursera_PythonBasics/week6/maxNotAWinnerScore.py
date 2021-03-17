a = open('input.txt', 'r', encoding='utf8')
max1 = [0] * 12
max2 = [0] * 12
for line in a:
    klass = int(line.split()[-2])
    ball = int(line.split()[-1])
    if ball > max1[klass]:
        max2[klass] = max1[klass]
        max1[klass] = ball
    elif ball > max2[klass] and ball < max1[klass]:
        max2[klass] = ball
print(*max2[9:])
