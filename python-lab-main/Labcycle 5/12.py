n=int(input("enter the number\t"))
lst=[]
for i in range(n):
    lst.append(input("enter the color\t"))

print('first color is {} last color is {}'.format(lst[0],lst[-1]))