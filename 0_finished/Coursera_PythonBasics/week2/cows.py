n = int(input())
round = n % 10
if n >= 10 and n <= 14:
    print(n, 'korov', sep=' ')
elif round == 1:
    print(n, 'korova', sep=' ')
elif round >= 2 and round <= 4:
    print(n, 'korovy', sep=' ')
else:
    print(n, 'korov')
