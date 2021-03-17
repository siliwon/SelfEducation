n = int(input())
m = int(input())
k = int(input())
if k > (n * m):
    print('NO')
elif k % m == 0:
    print('YES')
elif k % n == 0:
    print('YES')
else:
    print('NO')
