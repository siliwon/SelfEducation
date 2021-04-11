class Person:

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender == 'male' or gender == 'female' or gender == None:
            self.gender = gender
        else:
            print('Не знаю, что вы имели в виду? '
                  'Пусть это будет мальчик!')
            self.gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f"Гражданин {self.surname} {self.name}"
        else:
            return f"Гражданка {self.surname} {self.name}"

p1 = Person('Chuck', 'Norris')
print(p1) # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2) # печатает "Гражданка Kunis Mila"
p3 = Person('Ivan', 'Norris')
print(p3)