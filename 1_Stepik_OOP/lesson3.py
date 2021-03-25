class Lion:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"the object - {self.name}"

    def __str__(self):
        return f"lion {self.name}"