#Task-1 Print only those employees whose salary is greater than 60000

import csv

#Reading The CSV File
with open("employee_data01.csv","r") as file:
    csv_reader=csv.reader(file)
    next(csv_reader)
    for i in csv_reader:
        salary=float(i[3])
        if(salary>60000):
    
            print("Salary greater than 65000:",i)

#sample output
# Salary greater than 65000: ['101', 'Arun', 'IT', '70000']
# Salary greater than 65000: ['102', 'Riya', 'HR', '65000']