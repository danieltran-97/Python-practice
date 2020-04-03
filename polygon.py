import turtle

class Polygon:
    def __init__(self, sides,name, size=100):
        self.sides = sides
        self.name = name
        self.size = size
        self.interior_angles = (self.sides -2) * 180
        self.angle = self.interior_angles/self.sides
    def draw(self):
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(180-self.angle)

square = Polygon(4, "Square")
pentagon = Polygon(5, "Pentagon")

print(square.sides)
print(square.name)
# print(square.interior_angles)
# print(square.angle)

print(pentagon.sides)
print(pentagon.name)
# pentagon.draw()
hexagon = Polygon(6, "Hexagon")
hexagon.draw()