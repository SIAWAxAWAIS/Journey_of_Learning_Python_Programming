import math
class Shape:
    def __init__(self , x , y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius , radius)

    # def area(self):
    #     return math.pi * self.radius * self.radius

    def area(self):
        return math.pi * super().area()

cir = Circle(5)
print(cir.area())
# rec = Shape(5 , 8)
# print(rec.area())