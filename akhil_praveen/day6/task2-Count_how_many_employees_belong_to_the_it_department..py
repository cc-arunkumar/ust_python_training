# Count how many employees belong to the IT department.
import csv
with open("employee_data01.csv","r") as file:
    csv_file = csv.reader(file)
    next(csv_file)
    count=0
    for row in csv_file:
        if row[2]>"IT":
            count+=1
    print("Number of employees belong to the IT department: ",count)
            
# output

# Number of employees belong to the IT department:  1