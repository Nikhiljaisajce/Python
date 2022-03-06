
class Rectangle:
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)


l1=float(input("Enter length of rectangle: "))
b1=float(input("Enter breadth of rectangle: "))
l2=float(input("Enter length of rectangle: "))
b2=float(input("Enter breadth of rectangle: "))
rect1=Rectangle(l1,b1)
rect2=Rectangle(l2,b2)
print("Area of rectangle 1 is {} and perimeter is {}: ".format(rect1.area(),rect1.perimeter()))
print("Area of rectangle 2 is {} and perimeter is {}: ".format(rect2.area(),rect2.perimeter()))
print(rect1.area()>rect2.area())
