# POLYMORPHISM --> GREEK WORD THAT MEANS TO "HAVE MANY FORMS OR FACES"

#  POLY --> MANY
#  MORPHE --> FORM

#       TWO WAYS TO ACHIEVE POLYMORPHISM 
#       1. INHERITANCES --> AN OBJECT COULD BE TREATED OF THE SAME TYPE AS A PARENT CLASS 
#       2. "DUCK TYPING" --> OBJECT MUST HAVE NECESSARY ATTRIBUTE / METHOD

from abc import ABC , abstractmethod

class shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(shape):
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius **2
    
class Square(shape):
    def __init__(self , side):
        self.side = side

    def area(self):
        return self.side **2
    

class Triangle(shape):
    def __init__(self , height , width):
        self.height = height
        self.width = width 

    def area(self):
        return 0.5 * self.height * self.width
    
shapes = [Circle(4) , Square(6) , Triangle(3,9)]

for shape in shapes:
    print(f"{shape.area()}")
    