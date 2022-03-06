newFile = open("States.txt","w")
newFile.write("Goa \nKerala \nTamilnadu \nBangal\nPunjab")
newFile.close()

readFile = open("States.txt","r")
lines = readFile.readlines()
print(lines)
readFile.close()

oddFile = open("oddcontent.txt","w")
for i in range(0,len(lines),2):
    oddFile.write(lines[i])
oddFile.close() 

readFile = open("oddcontent.txt","r")
lines = readFile.readlines()
print(lines)
readFile.close()