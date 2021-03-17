class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if isinstance(new_email, str) and new_email.count('@') == 1:
            if new_email.count('.', new_email.find('@')) == 1:
                self.__email = new_email
            else:
                print('Ошибочная почта')
        else:
            print('Ошибочная почта')

    email = property(fget=get_email, fset=set_email)


k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = 'hello@re.w3'
print(k.email)
