dict = {}
n = int(input())
for i in range(n):
    a = list(input().split())
    for d in range(1, len(a)):
        dict[a[d]] = a[0]
m = int(input())
g = []
for i in range(m):
    g.append(input())
for i in range(m):
    print(dict[g[i]])
