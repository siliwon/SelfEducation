class Counter:

    def start_from(self, count=0):
        self.count = count

    def increment(self):
        self.count += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.count}')

    def reset(self):
        self.count = 0