#Task 2:
#Count how many employees belong to the IT department.

import csv

with open("employee_data01.csv","r") as file:
    cs_data=csv.reader(file)
    next(cs_data)
    count=0
    for data in cs_data:
        if(data[2]=="IT"):
            count+=1
print("Total IT is :",count)

#Output
# Total IT is : 1