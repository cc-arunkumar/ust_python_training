# Employee Attendance Tracker
# (employee_id, employee_name, days_present)

attendance = (
 ("E101", "John", 5),
 ("E102", "Priya", 3),
 ("E103", "Amit", 4),
 ("E104", "Neha", 2)
)
# all employee names who attended 4 or more days.
count=0
for item in attendance:
    if item[2]>=4:
        print(item[1])
    else:
        count=count+1
print("Employees less than 4 days ",count)
# employee with max attendenace
mx=0
emp=""
for id,name,presnt in attendance:
    if presnt>mx:
        mx=presnt
        emp=name
print(f"Employee with highest attendance: {emp} ({mx} days)")

# //sample execution 
# John
# Amit
# Employees less than 4 days  2
# Employee with highest attendance: John (5 days)
