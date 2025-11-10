#employee directory system

employees={"E101":"arjun","E102":"Neha","E103":"Ravi"}
employees.update({"E104":"Priya","E105":"Ravi"})
print(employees)
employees.update({"E103":"Ravi Kumar"})
print(employees)
del employees["E102"]
print(employees)
total=len(employees)
print(total)
for unique_id,name in employees.items():
    print("employee ID",unique_id,"->",name)
employee_id=input("enter the id")
if employee_id not in employees:
    print(employee_id, "is not found")
else:
    print(employees[employee_id])

#sample output

# {'E101': 'arjun', 'E102': 'Neha', 'E103': 'Ravi', 'E104': 'Priya', 'E105': 'Ravi'}  
# {'E101': 'arjun', 'E102': 'Neha', 'E103': 'Ravi Kumar', 'E104': 'Priya', 'E105': 'Ravi'}
# {'E101': 'arjun', 'E103': 'Ravi Kumar', 'E104': 'Priya', 'E105': 'Ravi'}
# 4
# employee ID E101 -> arjun
# employee ID E103 -> Ravi Kumar
# employee ID E104 -> Priya
# employee ID E105 -> Ravi
# enter the id110
# 110 is not found
