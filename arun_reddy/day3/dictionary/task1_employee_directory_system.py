employees={"E101": "Arjun","E102": "Neha","E103": "Ravi"}
# dd two new employees:
employees["E104"]="Priya"
employees["E105"]="Vikram"
print(employees)
#updation
employees["E103"]="RaviKumar"
print(employees)
# remove
del employees["E102"]
print(employees)
# length 
print(len(employees))

for empid,name in employees.items():
    print(f"Employee ID: {empid} → Name: {name}")

print(employees.get("E110","Employee Not found"))


