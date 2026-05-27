import calculater, hexagon, rectangle, square, triangle, circle

try:
    hex = hexagon.Hexagon(7)
    sqre = square.Square(2,9,4)
    rect = rectangle.Rectangle(2,3)
    trngl = triangle.Triangle(1,2,3,4,5,6)
    crlce = circle.Circle(1)
    shape = calculater.Shape()
except ValueError as e:
    print(e)
else:
    print(hex)
    print(sqre)
    print(rect)
    print(trngl)
    print(crlce)
    print(repr(rectangle))

