# Task 1: Employee Attendance Tracker
# Your HR system stores each employee’s attendance record for a week as a tuple

# Tuple storing employee attendance data (ID, Name, Days Attended)
attendance = (("E101", "Deva", 3), ("E102", "Raj", 5), ("E103", "Gokul", 7))

# Initialize a counter for employees attending less than 4 days
count = 0

# Check and print employees who attended more than 4 days
for i, j, k in attendance:
    if k > 4:
        print("Attended more than 4 days: ", j)

# Count the number of employees who attended less than 4 days
for i, j, k in attendance:
    if k < 4:
        count += 1

# Print the count of employees who attended less than 4 days
print("Present less than 4 days: ", count)

# Find the employee with the highest attendance
maxi = 0  # Initialize variable to store max attendance
for i, j, k in attendance:
    if k > maxi:
        maxi = k  # Update the highest attendance value

# Print the employee with the highest attendance
print("Employee with highest attendance: ", maxi)


#Sample output

# Attended more than 4 days:  Raj
# Attended more than 4 days:  Gokul
# Present less than 4 days:  1
# Employee with highest attendance:  Gokul