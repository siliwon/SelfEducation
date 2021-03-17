A = int(input())
B = int(input())
while A != B:
    while (A // 2) >= B and (A % 2) == 0:
        A = A // 2
        print(':2')
    if A > B:
        A -= 1
        print('-1')
