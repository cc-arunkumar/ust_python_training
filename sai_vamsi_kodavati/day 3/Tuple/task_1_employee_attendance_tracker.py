# TASK 1 - : Employee Attendance Tracker

tuple1 = ("E101","John",5),("E102","Priya",3),("E103","Amit",4),("E104","Neha",2)

print("Employees with attendance >= 4 days:")
for emp_id,emp_name,days_present in tuple1:
    if days_present >= 4:
        print(emp_name)

count = 0
for emp_id,emp_name,days_present in tuple1:
    if days_present < 4:
        count += 1
        
print("Employees were present less than 4 days:",count)

for emp_id,emp_name,days_present in tuple1:
    if days_present > 4:
        print(f"Employee with Highest attendance:{emp_name} ({days_present} days)")

# ----------------------------------------------------------------------------------

# Sample Output

# Employees with attendance >= 4 days:
# John
# Amit
# Employees were present less than 4 days: 2
# Employee with Highest attendance:John (5 days)