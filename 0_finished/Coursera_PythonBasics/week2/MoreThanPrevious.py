n = int(input())
k = 0
i = 0
while n != 0:
    if n == 0:
        print(0)
    else:
        k = n
        n = int(input())
        if n > k:
            i += 1
        else:
            continue
print(i)
