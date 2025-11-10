# Task 1: Employee Attendance Tracker
attendance = (
 ("E101", "John", 5),
 ("E102", "Priya", 3),
 ("E103", "Amit", 4),
 ("E104", "Neha", 2)
)
# employee_id, employee_name, days_present=attendance
count=0
max=0
for employee_id, employee_name, days_present in attendance:
    # 1. Print all employee names who attended 4 or more days.
    if days_present>=4:
        print("Employee Name:", employee_name)
    # 2. Count how many employees were present less than 4 days.
    if days_present<4:
        count+=1
    # 3. Find the employee with maximum attendance using a simple loop.
    if days_present>max:
        max=days_present
        name=employee_name
print(count)
print(f"Employee with highest attendance: {name}({max} days)")
# Sample output
#     Employee Name: John
# Employee Name: Amit
# 2
# Employee with highest attendance: John(5 days)