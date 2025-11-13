#Task 1: Employee Directory System
employees={"E101": "Arjun","E102": "Neha","E103": "Ravi"}
employees["E104"]="Priya"
employees["E105"]="Vikram"
employees["E103"]="Ravi Kumar" 
del(employees["E102"])
print("Total number of Employees: ",len(employees))

for emp_id,emp_name in employees.items():
    if(emp_id=="E110"):
        print("Employee not found")
    print(f"Employee ID:{emp_id}--->Name: {emp_name}")

#Sample Executions
# Total number of Employees:  4
# Employee ID:E101--->Name: Arjun
# Employee ID:E103--->Name: Ravi Kumar
# Employee ID:E104--->Name: Priya
# Employee ID:E105--->Name: Vikram

