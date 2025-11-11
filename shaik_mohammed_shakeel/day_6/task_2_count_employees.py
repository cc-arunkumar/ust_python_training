# Task 2 Count how many employees belong to the IT department

import csv
count=0
with open("employee_data01.csv","r") as file:
    csv_reader=csv.reader(file)
    next(csv_reader)
    for i in csv_reader:
        if (i[2]=="IT"):  
            count+=1
            
print("The number of employees belongs to IT: ",count)

#Sample output
# The number of employees belongs to IT:  1