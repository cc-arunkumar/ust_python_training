#Task 1: Employee Attendance Tracker
attendance = (
 ("E101", "John", 5),
 ("E102", "Priya", 3),
 ("E103", "Amit", 4),
 ("E104", "Neha", 2)
)
max=0
name="k"
for(employee_id, employee_name, days_present) in attendance:
    if(days_present>max):
        name=employee_name
        max=days_present

print("Employee with highest attendance: ",name,"(",max,"days )")

#Sample output
#Employee with highest attendance:  John ( 5 days )