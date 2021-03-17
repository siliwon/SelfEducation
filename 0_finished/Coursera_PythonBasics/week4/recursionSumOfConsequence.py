def consequence():
    summary = 0
    n = int(input())
    if n != 0:
        summary = n + consequence()
    return summary


print(consequence())
