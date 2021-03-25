class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return int(self.total_cents // 100)

    @dollars.setter
    def dollars(self, amount):
        if isinstance(amount, int) and amount >= 0:
            dollars = amount
            cents = self.total_cents % 100
            self.total_cents = dollars * 100 + cents
        else:
            print('Error dollars')

    @property
    def cents(self):
        return int(self.total_cents % 100)

    @cents.setter
    def cents(self, amount):
        if isinstance(amount, int) and amount < 100:
            dollars = self.total_cents // 100
            cents = amount
            self.total_cents = dollars * 100 + cents
        else:
            print('Error cents')

    def __str__(self):
        return f"Ваше состояние составляет {self.total_cents // 100}" \
               f" долларов {self.total_cents % 100} центов"


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов