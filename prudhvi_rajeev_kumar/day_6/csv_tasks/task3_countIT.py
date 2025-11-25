import csv

#The task was to read the 
count = 0
with open('employeedata01.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        if row[2] == 'IT':
            count += 1
print("Employees Belong to IT dept : ", count)