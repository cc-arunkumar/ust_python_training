
# Task:1 employees who salary is greater than 60000
# import csv to use it
import csv

# open the file in read mode

with open('employee_data01.csv',mode='r') as file:
    csv_reader=csv.reader(file)
    next(csv_reader)
    print(csv_reader)

    for line in file:
        each_line=line.strip().split(",")
        if int(each_line[3])>60000:
            print(each_line)

# sample output:
# ['101', 'Arun', 'IT', '70000']
# ['102', 'Riya', 'HR', '65000']