color1 = ["White", "Black", "Red"]
color2 = ["Red", "green"]
print("Colour list is")
print(color1)
print(color2)
print("colours not in 2nd list is:\t")
for z in color1:
    if z not in color2:
        print(z)