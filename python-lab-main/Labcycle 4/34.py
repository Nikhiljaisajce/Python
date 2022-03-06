

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.area=length*width

    def __lt__(self, other):
        if self.area<other.area:
            return "Reactangle 1 is smaller in Area"
        else:
            return "Reactangle 2 is smaller in Area"
r1=Rectangle(50,20)
r2=Rectangle(30,10)
print(r1<r2)




