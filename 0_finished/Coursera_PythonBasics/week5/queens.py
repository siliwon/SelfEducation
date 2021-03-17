def check(x, y):
    k = 1
    for j in x:
        if x.count(j) > 1 or y.count(j) > 1:
                return "YES"
    for i in range(7):
        for n in range(k, 7):
            if abs(x[i]-x[n]) == abs(y[i]-y[n]):
                return "YES"
        k += 1
    return "NO"


x = []
y = []
for i in range(8):
    n = list(map(int, input().split()[:2]))
    x.append(n[0])
    y.append(n[1])
print(check(x, y))
