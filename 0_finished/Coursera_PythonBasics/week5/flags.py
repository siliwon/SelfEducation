n = int(input())
i = 1
print('+___ ' * n, sep=' ')
for i in range(1, n + 1):
    print('|' + str(i) + ' / ', end='')
print()
print('|__\ ' * n, sep=' ')
print('|    ' * n, sep=' ')
