class Polygon:
    def __init__(self, sides, type):
        self.sides = sides
        self.type = type
        self.length = []

    def area(self):
        if self.type == "Triangle":
            s = sum(self.length) / 2
            area = (s * (s - self.length[0]) * (s - self.length[1]) * (s - self.length[2])) ** 0.5
            return area
        elif self.type == "Rectangle":
            area = self.length[0] * self.length[1]
            return area
        elif self.type == "Square":
            area = self.length[0] ** 2
            return area

class Triangle(Polygon):
    def __init__(self, length):
        super().__init__(3, "Triangle")
        self.length = length

class Rectangle(Polygon):
    def __init__(self, length):
        super().__init__(4, "Rectangle")
        self.length = length

class Square(Polygon):
    def __init__(self, length):
        super().__init__(4, "Square")
        self.length = length

t = Triangle([3, 4, 5])
print("Triangle area:", t.area())

r = Rectangle([3, 4])
print("Rectangle area:", r.area())

s = Square([3])
print("Square area:", s.area())
