#CSV File ==>Comma Separated Values file

import csv

#Reading CSV File

with open('employee_data01.csv',mode='r') as file:
    csv_reader=csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        print(row)

#sample Output
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha> & 
# "C:/Program Files/Python314/python3.14t.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day6/csv_reader.py
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']
# ['103', 'John', 'Finance', '60000']
# ['104', 'Neha', 'Marketing', '55000']
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha> 
