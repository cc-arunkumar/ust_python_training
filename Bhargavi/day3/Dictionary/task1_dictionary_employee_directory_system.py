#Employee Directory System
employees = {"E101": "Arjun","E102": "Neha","E103": "Ravi"}
employees["E104"] = "Priya"
employees["E105"] = "Vikaram"

employees["E103"] = "RAvi Kumar"

employees.pop("E102")

total_employees = len(employees)
print(total_employees)

print("Final employee list: ")
for emp_id , name in employees.items():
    print(f"Employee ID : {emp_id} -> Name: {name} ")

search_id = "E110"
if search_id in employees:
    print(f"\nEmployee ID: {search_id} -> Name: {employees[search_id]}")
else:
    print("\nEmployee not found")

# 4
# Final employee list: 
# Employee ID : E101 -> Name: Arjun 
# Employee ID : E103 -> Name: RAvi Kumar 
# Employee ID : E104 -> Name: Priya 
# Employee ID : E105 -> Name: Vikaram 

# Employee not found