n = int(input())
i = 0
while n != 0:
    if n == 0:
        break
    elif n % 2 == 0:
        i += 1
        n = int(input())
    else:
        n = int(input())
        continue
print(i)
