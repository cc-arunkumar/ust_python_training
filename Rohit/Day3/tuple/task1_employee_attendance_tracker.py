# Task 1: Employee Attendance Tracker
# Scenario:
# Your HR system stores each employee’s attendance record for a week as a tuple# Step 1: Initialize a tuple of employee attendance records
employee_week = (
    ("E101", "John", 5),
    ("E102", "Priya", 3),
    ("E103", "Amit", 4),
    ("E104", "Neha", 2)
)

# Step 2: Initialize variables to track highest attendance and low attendance count
max_days = -1             # Stores the maximum number of days present
top_employee = ''         # Stores the name of the employee with highest attendance
low_attendance_count = 0  # Counts employees with less than 4 days present

# Step 3: Iterate through each employee record
print("Print employees with good attendance ")
for employee in employee_week:
    employee_id, employee_name, days_present = employee

    # Step 4: Update top employee if current has more days present
    if days_present > max_days:
        max_days = days_present
        top_employee = employee_name

    # Step 5: Print employees with good attendance (>= 4 days)
    
    if days_present >= 4:
        print(employee_name)
    else:
        # Step 6: Count employees with low attendance (< 4 days)
        low_attendance_count += 1

# Step 7: Display the employee with the highest attendance
print(f"Employee with highest attendance: {top_employee} ({max_days} days)")


# =============sample output =====================
# Print employees with good attendance 
# John
# Amit
# Employee with highest attendance: John (5 days)
