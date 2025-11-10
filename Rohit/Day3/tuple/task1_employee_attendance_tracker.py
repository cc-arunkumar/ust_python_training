employee_week = (
    ("E101", "John", 5),
    ("E102", "Priya", 3),
    ("E103", "Amit", 4),
    ("E104", "Neha", 2)
)

max_days = -1
top_employee = ''
low_attendance_count = 0

for employee in employee_week:
    employee_id, employee_name, days_present = employee

    if days_present > max_days:
        max_days = days_present
        top_employee = employee_name

    if days_present >= 4:
        print(employee_name)
    else:
        low_attendance_count += 1

print(f"Employee with highest attendance: {top_employee} ({max_days} days)")



# =============sample output =====================
# John
# Amit
# Employee with the highest attendance: John (5 days)
