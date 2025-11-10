#Task 1: Employee Directory System
employees={
    "E101": "Arjun",
    "E102": "Neha",
    "E103": "Ravi"
}
employees["E104"]="Priya"
employees["E105"]="Vikram"
employees["E103"]="Ravi Kumar"
employees.pop("E102")
print(f"Total EMP : {len(employees)}")
for i in employees:
    print(f"Employee ID: {i} → Name: {employees.get(i)}")

print(employees.get("E110","Employee not found"))
#Output
# Total EMP : 4
# Employee ID: E101 → Name: Arjun
# Employee ID: E103 → Name: Ravi Kumar
# Employee ID: E104 → Name: Priya
# Employee ID: E105 → Name: Vikram
# Employee not found