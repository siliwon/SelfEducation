print(
    *map(
        lambda x: abs(x[0] - x[1]),
        zip(
            list(
                map(
                    int,
                    input().split()
                )
            ),
            list(
                map(
                    int,
                    input().split()
                )
            )
        )
    )
)
