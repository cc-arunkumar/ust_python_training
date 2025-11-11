# Task 1:
# Print only those employees whose salary is greater than 60000.

import csv

# id,name,department,salary
# 101,Arun,IT,70000
# 102,Riya,HR,65000
# 103,John,Finance,60000
# 104,Neha,Marketing,55000

with open("employee_data01.csv","r") as file:
    csv_reader =csv.reader(file)
    next(csv_reader)
    print(csv_reader)
    
    for line in file:
        each_line=line.strip().split(",")
        if each_line[3]>60000:
            print(each_line)
   
     
            
             
