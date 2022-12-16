import math

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'Dot: {self.x, self.y}'


class Circle:
    def __init__(self, r):
        self.r = r

    def radius(self):
        b = math.pi * (self.r ** 2)
        return '%.2f' % b


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b





p1 = Dot(1, 2)
p2 = Dot(1, 2)
print(p1 == p2)
print(str(p1))
print(p2)

r1 = Circle(20)
r2 = Circle(10)

print(r1.radius())
print(r2.radius())

rec1 = Rectangle(10,20)
rec2 = Rectangle(10,20)

print(rec1.get_area())

print(rec1 == rec2)