n = list(map(int, input().split()))
k = n[1]
n = int(n[0])
skt = []

for i in range(n):
    skt.append('I')

for i in range(k):
    a = list(map(int, input().split()))
    a1 = a[0] - 1
    a2 = a[1]
    for j in range(a1, a2):
        skt[j] = '.'
skittles = ''
skittles = skittles.join(skt)
print(skittles)
