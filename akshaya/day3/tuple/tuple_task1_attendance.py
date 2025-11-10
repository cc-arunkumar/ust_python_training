# Task 1: Employee Attendance Tracker

attendance = (
    ("E101", "John", 5),
    ("E102", "Priya", 3),
    ("E103", "Amit", 4),
    ("E104", "Neha", 2)
)


print("Employees with 4 or more days of attendance:")
for emp_id, name, days in attendance:
    if days >= 4:
        print(name)


count_less_than_4 = 0
for emp_id, name, days in attendance:
    if days < 4:
        count_less_than_4 += 1
print("\nNumber of employees with less than 4 days attendance:", count_less_than_4)


max_days = 0
max_employee = ""
for emp_id, name, days in attendance:
    if days > max_days:
        max_days = days
        max_employee = name


print(f"\nEmployee with highest attendance: {max_employee} ({max_days} days)")

#sample output
# PS C:\Users\303375\Downloads\Tasks> python tuple_task1_attendance.py
# Employees with 4 or more days of attendance:
# John
# Amit

# Number of employees with less than 4 days attendance: 2

# Employee with highest attendance: John (5 days)
