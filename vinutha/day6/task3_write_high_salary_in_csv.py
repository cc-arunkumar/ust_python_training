# Task 3:
# Write the filtered data (salary > 60000) into a new file high_salary.csv.

import csv

high_salary_rows = []
# Reading input data from csv file
with open('employee_data01.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        salary = float(row['salary'].strip())
        if salary > 60000:
            high_salary_rows.append(row)
# writing output data into the csv file
with open('high_salary.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=high_salary_rows[0].keys())
    writer.writeheader()
    writer.writerows(high_salary_rows)

print(f"Written {len(high_salary_rows)} employees with salary > 60000 to high_salary.csv")

# #sample output
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> & "C:/Program Files/Python314/python3.14t.exe" c:/Users/Administrator/Desktop/Training/ust_python_training/vinutha/day6/task3_write_high_salary_in_csv.py
# Written 2 employees with salary > 60000 to high_salary.csv
# PS C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day6> 


#  high_Salary.csv Output
# id,name,department,salary
# 101,Arun,IT,70000
# 102,Riya,HR,65000