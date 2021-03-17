import itertools

print(
    *map(
        lambda x: ''.join(x),
        itertools.permutations(
            ''.join(
                map(
                    str,
                    range(
                        1,
                        1 + int(
                            input()
                        )
                    )
                )
            )
        )
    ),
    sep='\n'
)
