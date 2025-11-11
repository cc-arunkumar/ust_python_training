# Task 1:

# Print only those employees whose salary is greater than 60000.

# importing csv
import csv

# openong the csv file in read mode
with open("employee_data01.csv","r") as file:
    csv_reads=csv.reader(file)
    # using next to skip the first line (naming category)
    next(csv_reads)
    # iterating oevr the fileds of the csv
    for row in csv_reads:
        list1=list(row)
        #checking over the condition of salary greater than 60000
        if int(list1[3])>60000:
            #printing down the output 
            print("Salary Greater than 60000:",list1[1])
            
            

# sample execution
# Salary Greater than 60000: Arun
# Salary Greater than 60000: Riya


# Task 2:

# Count how many employees belong to the IT department.
import csv

import csv
with open("employee_data01.csv","r") as file:
    csv_reads=csv.reader(file)
    next(csv_reads)
    for row in csv_reads:
        list1=list(row)
        if list1[2]=="IT":
            print("employees belong to IT:",list1[1])
            
            
# sample execution 
# employees belong to IT: Arun


# Task 3:

# Write the filtered data (salary > 60000) into a new file high_salary.csv

import csv

# declaring a list
data=[]
# opeing the csv file to read the csv values 
with open("employee_data01.csv","r") as file:
    csv_reads=csv.reader(file)
    next(csv_reads)
    # iterating over the csv  file 
    for row in csv_reads:
        list1=list(row)
        # checking teh condition
        if int(list1[3])>60000:
            # appending to data 
            data.append(list1)

with open("output.csv","w",newline='') as file:
    csv_write=csv.writer(file)
    csv_write.writerows(data)
            
            
            
            
# smaple execution 
# 101,Arun,IT,70000
# 102,Riya,HR,65000