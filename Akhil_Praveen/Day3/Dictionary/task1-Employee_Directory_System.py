emp_dict={"E101": "Arjun",
"E102": "Neha",
"E103": "Ravi"}

emp_dict["E104"]= "Priya"
emp_dict["E105"]="Vikram"
emp_dict["E103"] =  "Ravi Kumar"
del emp_dict["E102"]
print("total number of employee: ",len(emp_dict))
for i in emp_dict:
    print(f"Employee ID: {i} → Name: {emp_dict[i]}")

# total number of employee:  4
# Employee ID: E101 → Name: Arjun
# Employee ID: E103 → Name: Ravi Kumar
# Employee ID: E104 → Name: Priya
# Employee ID: E105 → Name: Vikram