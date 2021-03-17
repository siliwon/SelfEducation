list = list(map(int, input().split()))
volume = list[0]
users = list[1]
user_volume = []
for i in range(users):
    user_volume.append(int(input()))
if sum(user_volume) <= volume:
    print(len(user_volume))
else:
    user_volume.sort()
    counter = 0
    for i in user_volume:
        if volume - i >= 0:
            counter += 1
            volume -= i
    print(counter)
