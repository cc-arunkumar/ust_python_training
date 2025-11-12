# task:1
# Print only those employees whose salary is greater than 60000.

import csv
#Reading the Csv file
with open('employee_data01.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    # removing the header details
    next(csv_reader)
    # printing the employee whose salary is greater than 60000  
    for row in csv_reader:
        salary = int(row[3])  
        if salary > 60000:
            print(row[1], salary, row[2]) 

# sample output
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> & "C:/Program Files/Python314/python3.14t.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day6/task1_employee_salary.py   
# Arun 70000 IT
# Riya 65000 HR
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> 
