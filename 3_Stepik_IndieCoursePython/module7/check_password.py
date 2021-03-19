def check_password(string: str):
    digits = 0
    uppercase = 0
    crazy_string = '!@#$%*'
    crazy = 0

    for i in string:
        if i in crazy_string:
            crazy += 1
        elif i.isdigit():
            digits += 1
        elif i.isupper():
            uppercase += 1

    def check_password(string: str):
        digits = 0
        uppercase = 0
        crazy_string = '!@#$%*'
        crazy = 0

        for i in string:
            if i in crazy_string:
                crazy += 1
            elif i.isdigit():
                digits += 1
            elif i.isupper():
                uppercase += 1

        if len(string) < 10 or digits < 3 or uppercase == 0 or crazy == 0:
            return 'Easy peasy'
        return 'Perfect password'


check_password('Qwerty1357!')