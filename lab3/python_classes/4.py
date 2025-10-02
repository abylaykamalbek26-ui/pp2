import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates:({self.x,self.y})")    
    def move(self,new_x,new_y):
        self.x = new_x
        self.y = new_y
    def dist(self,other_point):
        return  math.sqrt(abs(self.x-other_point.x)**2+abs(self.y-other_point.y)**2)   
    

x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

p1 = Point(x1,y1)
p2 = Point(x2, y2)
p1.show()
p2.show()
print(f"Distance between points: {p1.dist(p2)}")
p1.move(0, 0)
p1.show()