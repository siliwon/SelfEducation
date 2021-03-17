biggest_number = int(input())
result = set(str(i) for i in range(1, biggest_number + 1))
reaction = None
numbers = set(input().split())
while reaction != 'HELP':
    reaction = input().strip()
    if reaction == 'YES':
        result &= numbers
    elif reaction == 'NO':
        for i in numbers:
            result -= numbers
    string = input().strip()
    if string == 'HELP':
        break
    else:
        numbers = set(string.split())
print(*sorted(result))


def namber():
    w = set(range(1, int(input()) + 1))
    n = input().split()
    while n != 'HELP':
        answer = str(input())
        if answer == "YES":
            w &= set(map(int, n))
        elif answer == "NO":
            w -= set(map(int, n))
        n = input().split()
        if str(n[0]) == 'HELP':
            return map(int, w)


print(*sorted(namber()))