# employee_attendance_tracker

attendance = (
 ("E101", "John", 5),
 ("E102", "Priya", 3),
 ("E103", "Amit", 4),
 ("E104", "Neha", 2)
)
count=0
employee=""
day=0

    
print("Employees who attended 4 or more days.")
for (emp_id,name,days) in attendance:
    if days>=4:
        print(name)
    else:
        count+=1
    if day<days:
        employee=name
        day=days
print("count of employees attandence less than 4: ",count)
print(f"Employee with highest attendance: {employee} ({day} days)")

# Employees who attended 4 or more days.
# John
# Amit
# count of employees attandence less than 4:  2
# Employee with highest attendance: John (5 days)
