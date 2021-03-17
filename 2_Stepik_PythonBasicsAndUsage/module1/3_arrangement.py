import itertools


n, k = map(int, input().split())
print(len([*itertools.combinations(range(n), k)]))