import csv

#The task was to read the employees 
with open('employeedata01.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        print(row)
