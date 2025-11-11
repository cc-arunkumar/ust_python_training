# Task 1:

# Print only those employees whose salary is greater than 60000.
import csv
with open("employee_data01.csv","r") as file:
    csv_file = csv.reader(file)
    next(csv_file)
    for row in csv_file:
        if int(row[3])>60000:
            print(row[1])
            
            
# output
# Arun
# Riya