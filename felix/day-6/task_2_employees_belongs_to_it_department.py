# Employees works for IT department

import csv

with open("employee_data.csv","r") as file:
    csv_reader = csv.reader(file)
    
    
    # remove first row
    next(csv_reader)
    
    count = 0 # count variable for number of employees
    
    # iterating through each row of data
    for row in csv_reader:
        if row[2] == "IT":
            count += 1
            
    print("Employees works for IT department: ",count)
    
# output

# Employees works for IT department:  1