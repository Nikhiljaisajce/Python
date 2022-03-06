a=int(input("enter the limit\t"))
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
    
for i in range(a-1, 0,-1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print("\n")