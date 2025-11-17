courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}

unique_emp_names = set()

courses["Data Science"] = ["Arjun","vikram"]


courses["Python"].append("fatima")
courses["Python"].remove("Neha")

for key,val in courses.items():
    print(f"{key} → {val}")

for unique in courses.values():
    for name in unique:
        unique_emp_names.add(name.upper())

        
print(f"Employees with unique names are:{unique_emp_names}")



