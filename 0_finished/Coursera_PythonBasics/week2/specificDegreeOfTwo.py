n = int(input())
if 0 <= n <= 1:
    print('YES')
else:
    i = 1
    while 2 ** i <= n:
        if 2 ** i == n:
            print('YES')
            break
        elif 2 ** i < n:
            i += 1
            continue
        else:
            print('NO')
    else:
        print('NO')
