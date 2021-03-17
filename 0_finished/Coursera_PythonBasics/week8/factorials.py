import math

print(
    *map(
        math.factorial,
        range(
            int(input()) + 1)
    )
)
