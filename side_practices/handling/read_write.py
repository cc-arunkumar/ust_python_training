import datetime
import os

file_path = "side_practices\\handling\\employees.txt"

# emp_id = input("Enter Employee ID:")
# emp_name = input("Enter Name:")
# emp_dep = input("Enter Department:")
# emp_salary = int(input("Enter Salary:"))

# while True:
#     date_str = input("Enter valid date (YYYY-MM-DD):")

#     try:
#         y,m,d = map(int,date_str.split("-"))
#         joining_date = datetime.date(y,m,d)
#         print("joining date accepted :",joining_date)
#         break
#     except:
#         print("Invalid date.Try again")

#Adding Data to File
# with open(file_path,"a") as file:
#     file.write(f"\n{emp_id},{emp_name},{emp_dep},{emp_salary},{joining_date}")


#File Reading
# with open(file_path,"r") as file:
#     for line in file:
#         print(line.strip())


#Search Employee
n = input("Enter Employee ID: ")
with open(file_path,"r") as file:
    if n in file:
        print(file)