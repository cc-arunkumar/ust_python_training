# employee_directory_system
# UST’s HR team keeps employee details in a Python dictionary.
# Each employee has a unique ID and name.


employees={"E101": "Arjun","E102": "Neha","E103": "Ravi"}
employees["E104"]="Priya"
employees["E105"]="Vikram"
print(employees)
employees["E103"]="Ravi Kumar"
del employees["E102"]
print(len(employees))
for key,value in employees.items():
    print(f"Employee ID: {key}-->Name:{value}")
if employees.get("E100")==None:
    print("Employee not found") 



#Sample output

# {'E101': 'Arjun', 'E102': 'Neha', 'E103': 'Ravi', 'E104': 'Priya', 'E105': 'Vikram'}
# 4
# Employee ID: E101-->Name:Arjun
# Employee ID: E103-->Name:Ravi Kumar
# Employee ID: E104-->Name:Priya
# Employee ID: E105-->Name:Vikram
# Employee not found