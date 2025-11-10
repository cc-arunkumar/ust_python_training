#Task 1: Employee Directory System
employees={"E101": "Arjun","E102": "Neha","E103": "Ravi"}
employees["E104"]= "Priya"
employees["E105"]= "Vikram"
del employees["E102"]
print(len(employees))
for x in employees.items():
    print("Employee ID: ",x[0]," → Name: ",x[1])

print(employees.get("E110","Employee not found"))

#Sample output
# 4
# Employee ID:  E101  → Name:  Arjun
# Employee ID:  E103  → Name:  Ravi
# Employee ID:  E104  → Name:  Priya
# Employee ID:  E105  → Name:  Vikram
# Employee not found