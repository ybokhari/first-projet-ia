class Circle:
    pi = 3.14

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return Circle.pi * self._radius ** 2

circle = Circle(3)
print(circle.area())