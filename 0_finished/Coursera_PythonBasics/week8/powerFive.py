import functools

print(
    functools.reduce(
        lambda x, y: x * y,
        map(
            int,
            input().split()
        )
    )
    ** 5
)
