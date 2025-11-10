#Task 1: Employee Attendance Tracker

#Code 
attendance = (
    ("E101","John",5),
    ("E102","Priya",3),
    ("E103","Amit",4),
    ("E104","Neha",2)
)
count=0
for employee_id,employee_name,days_present in attendance:
    if(days_present>=4):
        print("Employee name who attended more than 4 days : ",employee_name)
    else:
        count+=1
print("Total no of employees less than 4 are : ",count)

high=0
emp_high=""
for employee_id, employee_name,days_present in attendance:
    if(high<days_present):
        high=days_present
for employee_id, employee_name,days_present in attendance:
        if(high==days_present):
             emp_high=emp_high+employee_name
print("Employee with highest attendance : ",emp_high)

#Sample Output
# Employee name who attended more than 4 days :  John
# Employee name who attended more than 4 days :  Amit
# Total no of employees less than 4 are :  2
# Employee with highest attendance :  John