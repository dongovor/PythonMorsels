import math

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        return (math.pi) * (self.radius) ** 2

    def diameter(self):
        return str(2 * self.radius)


c = Circle()
print(c.diameter())

c.radius = 5

print(c.diameter())
