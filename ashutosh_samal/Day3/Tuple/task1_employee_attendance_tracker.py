#Task 1: Employee Attendance Tracker

# Tuple representing employee attendance data (Employee ID, Name, Days Present)
attendance = (("E101", "John", 5), ("E102", "Priya", 3), ("E103", "Amit", 4), ("E104", "Neha", 2))

# Initialize a counter for employees with less than 4 days of attendance
count = 0

# Loop through each record in the attendance data
for id, name, days_present in attendance:
    # Check if the employee has attended 4 or more days
    if days_present >= 4:
        print("Employee with 4 or more days attendance:")
        print("Name:", name)

    # Count employees with less than 4 days of attendance
    if days_present < 4:
        count += 1

# After looping, print the number of employees who attended less than 4 days
print("Number of employees present less than 4 days:", count)

# Finding the employee with the highest attendance
max_attendance = attendance[0]  # Initialize with the first record

# Loop through each record to find the employee with the highest attendance
for record in attendance:
    if record[2] > max_attendance[2]:
        max_attendance = record

# Print the employee with the highest attendance
print(f"Employee with highest attendance: {max_attendance[1]} ({max_attendance[2]} days)")


#Sample Execution
# Employee with 4 or days attendance
# Name: John
# Employee with 4 or days attendance
# Name: Amit
# Number of employees present less than 4 days:  1
# Employee with highest attendance: John (5 days)