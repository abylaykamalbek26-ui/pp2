class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.width * self.length    

rectangle = Rectangle(6,7)

print(f"area of rectangle:{rectangle.area()}")