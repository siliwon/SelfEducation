n = int(input())
sum = 0
multiple = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        multiple *= j
    sum += multiple
    multiple = 1
if n == 0:
    print(1)
else:
    print(sum)
