class City:

    def __init__(self, name: str):
        self.name = name.title()

    def __str__(self):
        return f"{self.name}"

    def __bool__(self):
        return self.name[-1] != 'a' \
               and self.name[-1] != 'o' \
               and self.name[-1] != 'u' \
               and self.name[-1] != 'e' \
               and self.name[-1] != 'i'

p1 = City('new york')
print(p1)  # печатает "New York"
print(bool(p1))  # печатает "True"
p2 = City('SaN frANCISco')
print(p2)  # печатает "San Francisco"
print(p2 == True)  # печатает "False"
print(bool(p2))

# a = 'new yourk'
#
# print(a.title())

