
# Task 1: Employee Directory System
# Scenario:
# UST’s HR team keeps employee details in a Python dictionary.
# Each employee has a unique ID and name.

# Step 1: Initialize employee dictionary using keyword arguments
employee = dict(
    E101="Arjun",
    E102="Neha",
    E103="Ravi",
)

# Step 2: Add new employees using update()
employee.update(El04="priya")  # Note: 'El04' uses lowercase 'l'
employee.update(El05="vikram")

# Step 3: Update existing employee name
employee.update(E103="Ravi kumar")

# Step 4: Remove an employee by ID
del employee["E102"]

# Step 5: Display final employee dictionary
print(f"final employee dictionary {employee}")

# ============= sample output=============================
#final employee dictionary {'E101': 'Arjun', 'E103': 'Ravi kumar', 'El04': 'priya', 'El05': 'vikram'}