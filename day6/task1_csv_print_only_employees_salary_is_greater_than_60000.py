# Task 1:
# Print only those employees whose salary is greater than 60000.

import csv

with open('employee_data.csv', mode='r') as file:  #reading file
    csv_reader = csv.reader(file)
    next(csv_reader)  
    for row in csv_reader:
        salary = int(row[3])  
        if salary > 60000:
            print(row[1], salary, row[2]) 


#output
# Arun 70000 IT
# Riya 65000 HR