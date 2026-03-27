# Employee Attendance Tracker

# Task 1: Employee Attendance Tracker
# Scenario:
# Your HR system stores each employee’s attendance record for a week as a tuple.
# Each tuple contains:
# (employee_id, employee_name, days_present)
# Example data:
# attendance = (("E101", "John", 5),("E102", "Priya", 3),("E103", "Amit", 4),("E104", "Neha", 2))

# Your Tasks:
# 1. Print all employee names who attended 4 or more days.
# 2. Count how many employees were present less than 4 days.
# 3. Find the employee with maximum attendance using a simple loop.
# 4. Print the result in this format:
# Employee with highest attendance: John (5 days)


# Tuple of employee attendance records (emp_id, name, days_present)
attendance = (
    ("E101", "John", 5),
    ("E102", "Priya", 3),
    ("E103", "Amit", 4),
    ("E104", "Neha", 2)
)

# Print employees who attended 4 or more days
print("Employees who attended 4 or more days:")
for emp_id, name, days in attendance:
    if days >= 4:
        print(name)

# Count employees present less than 4 days
count = 0
for emp_id, name, days in attendance:
    if days < 4:
        count += 1
print("\nNumber of employees present less than 4 days:", count)

# Find employee with highest attendance
max_days = 0
max_name = ""
for emp_id, name, days in attendance:
    if days > max_days:
        max_days = days
        max_name = name

print(f"\nEmployee with highest attendance: {max_name} ({max_days} days)")


#  Output:
# Employees who attended 4 or more days:
# John
# Amit
#
# Number of employees present less than 4 days: 2
#
# Employee with highest attendance: John (5 days)
