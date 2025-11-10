#Task 1:Employee Directory System


#Code.
employee={
    "E101": "Arjun",
    "E102": "Neha",
    "E103": "Ravi"

}
employee["E104"]="Priya"
employee["E105"]="Vikram"
employee["E103"]= "Ravi Kumar"
del employee["E102"]
print("Total Employees : ",len(employee))
for emp_id,name in employee.items():
    print(f"Employee ID : {emp_id} = Name : {name}")
name = employee.get("E110","Employee not found")
print(name)

#Output 
# Total Employees :  4
# Employee ID : E101 = Name : Arjun
# Employee ID : E103 = Name : Ravi Kumar
# Employee ID : E104 = Name : Priya
# Employee ID : E105 = Name : Vikram
# Employee not found
