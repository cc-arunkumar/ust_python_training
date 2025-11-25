import csv


print("Employees Salary greater than 60k")
with open('employeedata01.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        if int(row[3]) > 60000:
            print(row)