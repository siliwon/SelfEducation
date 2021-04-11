class Zebra:

    def __init__(self):
        self.counter = 0

    def which_stripe(self):
        if self.counter % 2 == 0:
            print("Полоска белая")
            self.counter += 1
        else:
            print('Полоска черная')
            self.counter += 1
