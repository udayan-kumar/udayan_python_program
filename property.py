# PROPERTY --> DECORATOR USED TO DEFINE A METHOD AS A PROPERTY (IT CAN BE ACCESSED LIKE AN ATTRIBUTE)

# BENIFIT --> ADD ADDITIONAL LOGIC WHEN READ , WRITE , OR DELETE ATTRIBUTE .... GIVES YOU GETTER , SETTER AND DELETE METHOD

class Rectangle:

    def __init__(self , width , height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width}: .1f"
    
    @property
    def height(self):
        return f"{self.height}: .1f"
    
    @width.setter
    def width(self , new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width is greater than 0")

    @height.setter
    def height(self , new_height):
        if new_height > 0:
            self._width = new_height
        else:
            print("height is greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("width has been deleted")


    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")


rectangle = Rectangle(3,4)

rectangle.width = 4
rectangle.height = 10

del rectangle.width
del rectangle.height