# Task2
# Count how many employees belong to the IT department.
import csv
# Opening the file
with open('employee_data.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    count = 0
    for row in csv_reader:
        if row[2] == "IT":
          count += 1
    print("Number of employees having IT are:",count)
    
# Output
# Number of employees having IT are: 1