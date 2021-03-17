from functools import reduce

print(
    *map(
        lambda x: reduce(
            lambda z, y: z + y,
            map(int, x
                )
            ) % 2,
        zip(
            *map(
                lambda x: x.split(),
                open('input.txt').readlines()[1:]
            )
        )
    )
)