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
emplooyes={"E101": "Arjun",
"E102": "Neha",
"E103": "Ravi"}
emplooyes["E104"]= "Priya"
emplooyes["E105"]= "Vikram"
emplooyes["E103"]="Ravi Kumar"
emplooyes.pop("E102")

print(len(emplooyes))

for emp_id,emp_names in emplooyes.items():
    print(f"Employee Id:{emp_id}",f"emp_name:{emp_names}")

id=emplooyes.get("E110","Employee not found")
print(id)


# sample output
# 4
# Employee Id:E101 emp_name:Arjun
# Employee Id:E103 emp_name:Ravi Kumar
# Employee Id:E104 emp_name:Priya
# Employee Id:E105 emp_name:Vikram
# Employee not found

