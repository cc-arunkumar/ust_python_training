# Task 1: Employee Attendance Tracker
# Scenario:
# Your HR system stores each employee’s attendance record for a week as a tuple.
# Each tuple contains:
# (employee_id, employee_name, days_present)
# Example data:
# attendance = (
#  ("E101", "John", 5),
#  ("E102", "Priya", 3),
#  ("E103", "Amit", 4),
#  ("E104", "Neha", 2)
# )
# Your Tasks:
# 1. Print all employee names who attended 4 or more days.
# 2. Count how many employees were present less than 4 days.
# 3. Find the employee with maximum attendance using a simple loop.
# 4. Print the result in this format:
# Employee with highest attendance: John (5 days)
# Hints:
# Use tuple unpacking inside the loop:
# for emp_id, name, days in attendance:
#  # your logic here
# Keep track of the highest attendance using variables.


attendance = (("E101", "John", 5),("E102", "Priya", 3),("E103", "Amit", 4),("E104", "Neha", 2))
count=0
max=0
max_days=0
top_employee=""
# . Print all employee names who attended 4 or more day
for employee_id, employee_name, days_present in attendance:
    if days_present >4 :
        print("employees present more than 4 days:",employee_name)



# . Count how many employees were present less than 4 day
    if days_present<4:
        count+=1
        print("count of present less than 4:",count)



#  Print the result in this format
    if days_present>max:
        max=days_present
        name=employee_name
        print(f"Employee with highest attendance:({name}{max}days)")





# employees present more than 4 days: John
# Employee with highest attendance:(John5days)
# count of present less than 4: 1
# count of present less than 4: 2
