l=int(input("enter the num of names\t"))
counts=0
for i in range(l):
    a=input("enter the name\t").split(" ")[0]
    counts+=a.count('a')
print(counts)
