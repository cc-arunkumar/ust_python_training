#Task 1:Print only those employees whose salary is greater than 60000.
import csv

with open("employee_data01.csv","r") as file:
    cs_data=csv.reader(file)
    next(cs_data)
    for data in cs_data:
        if(int(data[3])>60000):
            print(data)

#Output
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']