first1 = int(input())
first2 = int(input())
second1 = int(input())
second2 = int(input())

if abs(second1 - first1) % 2 == abs(second2 - first2) % 2:
    print("YES")
else:
    print("NO")
