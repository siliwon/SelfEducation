n = int(input())
f_2 = 0
f_1 = 1
f = 0
i = 1
while f <= n:
    if f < n:
        f = f_1 + f_2
        f_2 = f_1
        f_1 = f
        i += 1
    elif f == n:
        print(i)
        break
else:
    print(-1)
