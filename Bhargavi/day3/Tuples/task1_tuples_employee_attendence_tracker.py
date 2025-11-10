# Employee Attendance Tracker
attendance = (("E101", "John", 5),("E102", "Priya", 3),("E103", "Amit", 4),("E104", "Neha", 2))
print("Employees who attended 4 or more days:")
for emp_id, name, days in attendance:
    if days >= 4:
        print(name)

count = 0
for emp_id, name, days in attendance:
    if days < 4:
        count += 1
print("\nNumber of employees present less than 4 days:", count)

max_days = 0
max_name = ""
for emp_id, name, days in attendance:
    if days > max_days:
        max_days = days
        max_name = name

print(f"\nEmployee with highest attendance: {max_name} ({max_days} days)")

# Employees who attended 4 or more days:
# John
# Amit

# Number of employees present less than 4 days: 2

# Employee with highest attendance: John (5 days)