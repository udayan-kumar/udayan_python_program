# SUPER() --> FUNCTON USED IN A CHILD CLASS TO CALL METHOD FROM A PARENT CLASS (SUPERCLASS) .... ALLOWS YOU TO EXTRNEXTEND THE FUNCTIONABLITY OF THE INHERITATED METHOD

class shape:
    def __init__(self , color , is_filled):
        self.color = color
        self.is_filled = is_filled

class circle(shape):
    def __init__(self, color, is_filled , radius):
        super().__init__(color , is_filled)
        self.radius = radius

class square(shape):
    def __init__(self, color, is_filled , width):
         super().__init__(color , is_filled)
         self.width = width

class triangle(shape):
    def __init__(self, color, is_filled , width , height):
        super().__init__(color , is_filled)
        self.width = width
        self.height = height


circle = circle(color = "red" , is_filled = True , radius = 5)
square = square(color = "black" , is_filled = False , width=10)
triangle = triangle(color = "blue" , is_filled = True , width=12 , height=43)

print(circle.color)
print(circle.is_filled)
print(circle.radius)

print(square.color)
print(square.is_filled)
print(square.width)

print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)