class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return str(self.name) + ' is ' + str(self.age) + ' years old'

    def speak(self, sound):
        return str(self.name) + ' says ' + sound
