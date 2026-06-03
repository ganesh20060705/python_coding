class Shape:
    pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing Rectangle")

class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")

Circle().draw()
Rectangle().draw()
Triangle().draw()