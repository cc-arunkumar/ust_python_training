"""
Task 1: Employee Attendance Tracker
Scenario:
Your HR system stores each employee’s attendance record for a week as a tuple.
Each tuple contains:
(employee_id, employee_name, days_present)
"""


attendance = (
 ("E101", "John", 5),
 ("E102", "Priya", 3),
 ("E103", "Amit", 4),
 ("E104", "Neha", 2)
)

for emp_id, name, days in attendance:
    if days>4:
        print(name)

emp_lessthan_4=0
for emp_id, name, days in attendance:
    if days<4:
        emp_lessthan_4+=1

print(f"{emp_lessthan_4} employees have Less than  4 day")

high_emp_name=""
high_emp_days=0

for emp_id, name, days in attendance:
    if days>high_emp_days:
        high_emp_days=days
        high_emp_name=name


print(f"Employee with highest attendance: {high_emp_name} ({high_emp_days}) days")


# sample output

"""
John
2 employees have Less than  4 day
Employee with highest attendance: John (5) days
"""