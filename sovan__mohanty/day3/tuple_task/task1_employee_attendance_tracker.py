#Task1 Employee Attendance Tracker
attendance=(
 ("E101", "John", 5),
 ("E102", "Priya", 3),
 ("E103", "Amit", 4),
 ("E104", "Neha", 2)
)
count1=0
for employee_id,employee_name,days_present in attendance:
    if(days_present>4):
        print("Employee attendance more than 4: ",employee_name)
    else:
        count1+=1
print("Number of employees with attendance less than 4: ",count1)
high=0
emp_high=""
for employee_id,employee_name,days_present in attendance:
    if(high<days_present):
        high=days_present
for employee_id,employee_name,days_present in attendance:
    if(high==days_present):
        emp_high=emp_high+employee_name
print(f"Employee with highest attendance: {emp_high} ({high} Days)")

#Sample Execution
# Employee attendance more than 4:  John
# Employee attendance more than 4:  Amit
# Number of employees with attendance less than 4:  3
# Employee with highest attendance: John (5 Days)
    