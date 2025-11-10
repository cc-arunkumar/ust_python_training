# Task 1- Employee Attendance Tracker

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


attendance = (("E101", "John", 5),("E102", "Priya", 3),("E103", "Amit", 4),("E104", "Neha", 2))
count=0
for eid,ename,dpresent in attendance:
    
    if(dpresent>=4):
        print( "Employees who attended 4 or more days:",ename) 
    else:
        count+=1
print("No.of Employees present less than 4 days:",count)
max_emp=max(attendance, key=lambda x:x[2])
print("Employee with highest attendance: ", max_emp[1])

#Output
# Employees who attended 4 or more days: John
# Employees who attended 4 or more days: Amit
# No.of Employees present less than 4 days: 2
# Employee with highest attendance:  John

