# #Task 1: Employee Attendance Tracker
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

attendance = (
 ("E101", "John", 5),
 ("E102", "Priya", 3),
 ("E103", "Amit", 4),
 ("E104", "Neha", 2)
)
max=0
name="k"
for(employee_id, employee_name, days_present) in attendance:
    if(days_present>max):
        name=employee_name
        max=days_present

print("Employee with highest attendance: ",name,"(",max,"days )")

#Sample output
#Employee with highest attendance:  John ( 5 days )