import math


def rectangle(length, width):
    area=length*width
    perimeter=2*(length+width)

    return "Area is {} and Perimeter is {}".format(area,perimeter)


def circle(r):
    area=math.pi*(r**2)
    perimeter=2*math.pi*r

    return "Area is {} and Perimeter is {}".format(area,perimeter)

def cuboid(length, breadth,height):
    area=2*((length*breadth)+(breadth+height)+(height*length))
    perimeter=4*(length+breadth+height)

    return "Area is {} and Perimeter is {}".format(area,perimeter)

def sphere(r):
    area=2*r
    perimeter=4*math.pi*(r**2)

    return "Area is {} and Perimeter is {}".format(area,perimeter)

