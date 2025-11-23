import csv
# TASK:2 count how many employees belongs to IT department

# id,name,department,salary
# 101,Arun,IT,70000
# 102,Riya,HR,65000
# 103,John,Finance,60000
# 104,Neha,Marketing,55000

with open("employee_data01.csv","r") as file:
    it_emp_count=0
    for line in file:
        each_line=line.strip().split(",")
        if each_line[2]=="IT":
            it_emp_count+=1
    print(f"The total employess in IT department is:{it_emp_count}")

# Sample output:
# The total employess in IT department is:1
