# Task 1: Employee Attendance Tracker
# Scenario:
# Your HR system stores each employee’s attendance record for a week as a tuple.


attendance = (
    ("E101", "John", 5),
    ("E102", "Priya", 3),
    ("E103", "Amit", 4),
    ("E104", "Neha", 2)
)
count = 0
maxi=0
maxi_name=""
print("Employees attended 4 or more days:") 

for id,name,num in attendance:
    if(num>maxi):
        maxi=num
        maxi_name=name
    if(num>=4):
         print(name)   
    if(num<4):
        count+=1
print(f"\nemployees were present less than 4 days are : {count}\n")
print(f"employee with maximum attendance: {maxi_name} ({maxi}days)")

# sample output:
# Employees attended 4 or more days:
# John
# Amit

# employees were present less than 4 days are : 2

# employee with maximum attendance: John (5days)