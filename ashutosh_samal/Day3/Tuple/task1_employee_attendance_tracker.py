#Task 1: Employee Attendance Tracker

attendance = (("E101", "John", 5), ("E102", "Priya", 3), ("E103", "Amit", 4), ("E104", "Neha", 2))
count=0
for id,name,days_present in attendance:
    if days_present>=4:
        print("Employee with 4 or days attendance")
        print("Name:",name)

if days_present<4:
    count+=1
    print("Number of employees present less than 4 days: ",count)    


max_attendance = attendance[0]

for record in attendance:
    if record[2] > max_attendance[2]:
        max_attendance = record
print(f"Employee with highest attendance: {max_attendance[1]} ({max_attendance[2]} days)")

#Sample Execution
# Employee with 4 or days attendance
# Name: John
# Employee with 4 or days attendance
# Name: Amit
# Number of employees present less than 4 days:  1
# Employee with highest attendance: John (5 days)