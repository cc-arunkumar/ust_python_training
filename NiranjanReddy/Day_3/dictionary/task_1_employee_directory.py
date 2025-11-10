# Task 1: Employee Directory System
employees={"E101": "Arjun","E102": "Neha","E103": "Ravi"}

employees["E104"]= "Priya"
employees["E105"]="Vikram"

employees["E103"]="Ravi Kumar"
del employees["E102"]
print(employees)

print(len(employees))
for key,value in employees.items():
    print(f"Employee ID: {key} -> Name: {value}")

id=employees.get("E110","Employee not found")
print(id)


# Sample output
# {'E101': 'Arjun', 'E103': 'Ravi Kumar', 'E104': 'Priya', 'E105': 'Vikram'}

# 4

# Employee ID: E101 -> Name: Arjun
# Employee ID: E103 -> Name: Ravi Kumar
# Employee ID: E104 -> Name: Priya
# Employee ID: E105 -> Name: Vikram

# Employee not found