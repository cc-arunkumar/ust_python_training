# Task 1: Employee Directory System


"""

Scenario:
UST’s HR team keeps employee details in a Python dictionary.
Each employee has a unique ID and name.

"""
employees={
    "E101": "Arjun",
    "E102": "Neha",
    "E103": "Ravi"
}

# Add
employees["E104"]="Priya"
employees["E105"]="Vikram"

print(employees)

#Update
employees["E103"]="Ravi Kumar"
print(employees)

del employees["E102"]
print(employees)

#Total
print(len(employees))

#FInal List
for key,value in employees.items():
    print(f"Employee ID: {key} → Name: {value}")

print(employees.get("E104", "Not found"))    


# sample output

"""
{'E101': 'Arjun', 'E102': 'Neha', 'E103': 'Ravi', 'E104': 'Priya', 'E105': 'Vikram'}
{'E101': 'Arjun', 'E102': 'Neha', 'E103': 'Ravi Kumar', 'E104': 'Priya', 'E105': 'Vikram'}
{'E101': 'Arjun', 'E103': 'Ravi Kumar', 'E104': 'Priya', 'E105': 'Vikram'}
4
Employee ID: E101 → Name: Arjun
Employee ID: E103 → Name: Ravi Kumar
Employee ID: E104 → Name: Priya
Employee ID: E105 → Name: Vikram
Priya

"""