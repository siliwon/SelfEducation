class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, other):
        if hasattr(other, 'set_coordinates'):
            return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5
        else:
            print("Передана не точка")
