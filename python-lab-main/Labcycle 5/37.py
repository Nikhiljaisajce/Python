file=open('demo.txt')
lst=[]
for line in file:
    lst.append(line)
print(lst)
file.close()