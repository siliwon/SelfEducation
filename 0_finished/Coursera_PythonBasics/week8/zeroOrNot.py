print(
    any(
        [
            list(
                filter(
                    lambda x: x.strip() == '0',
                    open(
                        'input.txt', 'r', encoding='utf-8')
                )
            )
        ]
    )
)
