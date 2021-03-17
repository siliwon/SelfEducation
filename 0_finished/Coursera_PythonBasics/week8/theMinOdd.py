print(
    min(
        filter(
            lambda x: x % 2 == 1,
            sorted(
                list(
                    map(
                        int,
                        input().split()
                    )
                )
            )
        )
    )
)
