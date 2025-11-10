# Task 1: Employee Directory System

# Scenario:
# UST’s HR team keeps employee details in a Python dictionary.
# Each employee has a unique ID and name.

# Instructions:
# 1. Create a dictionary named employees with:
# "E101": "Arjun"
# "E102": "Neha"
# "E103": "Ravi"
# 2. Add two new employees:
# "E104": "Priya"
# "E105": "Vikram"
# 3. Update "E103" to "Ravi Kumar" .
# 4. Remove "E102" .
# 5. Display the total number of employees.
# 6. Print the final list like:
# Employee ID: E101 → Name: Arjun
# 7. If "E110" is searched, print "Employee not found" .



employees={"E101": "Arjun","E102": "Neha","E103": "Ravi"}
print(employees)
employees["E104"]="Priya"
employees["E105"]="Vikram"
print(employees)
employees["E103"]="Ravi Kumar"
print(employees)
employees.pop("E102")
print(employees)
for eid, name in employees.items():
    print(f"Employee ID: {eid} → Name: {name}")
id=employees.get("E110","Employee Not found")
print(id)


#sample output
# {'E101': 'Arjun', 'E102': 'Neha', 'E103': 'Ravi'}
# {'E101': 'Arjun', 'E102': 'Neha', 'E103': 'Ravi', 'E104': 'Priya', 'E105': 'Vikram'}
# {'E101': 'Arjun', 'E102': 'Neha', 'E103': 'Ravi Kumar', 'E104': 'Priya', 'E105': 'Vikram'}
# {'E101': 'Arjun', 'E103': 'Ravi Kumar', 'E104': 'Priya', 'E105': 'Vikram'}
# Employee ID: E101 → Name: Arjun
# Employee ID: E103 → Name: Ravi Kumar
# Employee ID: E104 → Name: Priya
# Employee ID: E105 → Name: Vikram
# Employee Not found