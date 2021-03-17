n, k = map(int, input().split())
weekends = set()
all = set(range(1, n + 1))
for i in range(1, n + 1):
    if (i + 1) % 7 == 0:
        all.remove(i)
    if i % 7 == 0:
        all.remove(i)
zab = set()
for i in range(k):
    a, b = map(int, input().split())
    zab |= set(range(a, n + 1, b))
    zab &= all
print(len(zab))
