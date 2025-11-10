tuple1 = (
    ("E101", "John", 5),
    ("E102", "Priya", 3),
    ("E103", "Amit", 4),
    ("E104", "Neha", 2)
)

for emp_id, emp_name, days_present in tuple1:
   if days_present>=4:
       print(emp_name)



count=0
for emp_id, emp_name, days_present in tuple1:
    if days_present<4:
        count+=1
print(count,"employees were present less than 4 days.")



max_day=0
emp=""
for emp_id, emp_name, days_present in tuple1:
    if days_present>max_day:
        max_day=days_present
        emp=emp_name
        print(emp_name,"has the max attendance")


# John
# Amit
# 2 employees were present less than 4 days.
# John has the max attendance

