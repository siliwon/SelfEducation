n = int(input())
f_2 = 1
f_1 = 1
f = 0
i = 1
while i < n:
    f = f_1 + f_2
    f_2 = f_1
    f_1 = f
    i += 1
print(f_2)
