words=input("enter the sentance\t")
count={}.fromkeys(words.casefold().split(' '),0)
print(count)
for i in words.casefold().split(' '):
    count[i]+=1
print(count)
