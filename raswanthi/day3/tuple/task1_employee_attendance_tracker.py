#Task1: Employee Attendance Tracker
attendance=(("E101","John",5),("E102","Priya",3),("E103","Amit",4),("E104","Neha",2))

    
for emp_id, name, days in attendance:
    if days >= 4:
        print(name)

count = 0
for emp_id, name, days in attendance:
    if days < 4:
        count += 1
print(f"Number of employees present less than 4 days: {count}")

max_days = -1
max_employee = ""
for emp_id, name, days in attendance:
    if days > max_days:
        max_days = days
        max_employee = name
print(f"Employee with highest attendance: {max_employee} ({max_days} days)")


'''
Output:
John
Amit
Number of employees present less than 4 days: 2
Employee with highest attendance: John (5 days)
'''


