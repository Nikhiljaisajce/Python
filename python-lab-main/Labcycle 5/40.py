import csv
with open('employee.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Age", "Salary"])
    writer.writerow([121, "Revathy S", "26", "30000"])
    writer.writerow([122, "Arun Kumar", "24", "30000"])
with open('employee.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1] + " " + row[2])