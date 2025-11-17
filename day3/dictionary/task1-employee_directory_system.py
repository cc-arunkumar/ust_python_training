# Task 1: Employee Directory System
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

