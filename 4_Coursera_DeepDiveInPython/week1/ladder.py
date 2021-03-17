import sys


number = sys.argv[1]
for i in range(1, int(number) + 1):
    print(' ' * (int(number) - i), '#' * i, sep='')