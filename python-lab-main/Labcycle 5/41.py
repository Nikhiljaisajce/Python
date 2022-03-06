import csv
f = open("planets.csv","w",newline='')
writer = csv.DictWriter(f, fieldnames = ["Planet","count"])
writer.writeheader()
writer.writerow({"Planet":"Mercury", "count": "1"})
writer.writerow({"Planet": "Venus", "count": "2"})
writer.writerow({"Planet": "Earth", "count": "3"})
f.close()
c = 0
f = open("planets.csv")
reader = csv.DictReader(f)
for row in reader:
    if c==0:
        print(f'{"".join(row)}')
        c+=1
    print(f'{row["Planet"]},{row["count"]}')
    c+=1
print(c-1)
f.close()