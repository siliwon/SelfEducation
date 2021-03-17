length1 = int(input())
high1 = int(input())
length2 = int(input())
high2 = int(input())

if high2 <= high1:
    print('NO')
elif abs(high1 - high2) < abs(length1 - length2):
    print('NO')
elif abs((length1 % 2) - length2 % 2) != abs((high1 % 2) - high2 % 2):
    print('NO')
else:
    print('YES')
