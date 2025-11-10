# Task 1: Employee Directory System
# Scenario:
# UST’s HR team keeps employee details in a Python dictionary.
# Each employee has a unique ID and name.

# Step 1: Create the dictionary
Employes = {"E101": "Arjun", "E102": "Neha", "E103": "Ravi"}
print("Employes :", Employes)

# Step 2: Add two new employees
Employes["E104"] = "Priya"
Employes["E105"] = "Virkam"

# Step 3: Update "E103" to "Ravi Kumar"
Employes["E103"] = "Ravi kumar"
print("Employes :", Employes)

# Step 4: Remove "E102"
del Employes["E102"]
print(Employes)

# Step 5: Display the total number of employees and final list
total = len(Employes)
for emp_id, name in Employes.items():
    print(f"Employee ID: {emp_id}, Name: {name}")

# Step 6: Search safely for an employee
emp_search = Employes.get("E110", "Employee not found")
print("Search Result:", emp_search)


# Sample Output:
# Employes : {'E101': 'Arjun', 'E102': 'Neha', 'E103': 'Ravi'}
# Employes : {'E101': 'Arjun', 'E102': 'Neha', 'E103': 'Ravi kumar', 'E104': 'Priya', 'E105': 'Virkam'}
# {'E101': 'Arjun', 'E103': 'Ravi kumar', 'E104': 'Priya', 'E105': 'Virkam'}
# Employee ID: E101, Name: Arjun
# Employee ID: E103, Name: Ravi kumar
# Employee ID: E104, Name: Priya
# Employee ID: E105, Name: Virkam
# Search Result: Employee not found
