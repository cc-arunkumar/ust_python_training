courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
"Cloud": ["Neha", "Ravi", "Priya"]
}

courses["Data Science"] = ["Arjun", "Vikram"]
courses["Python"].append("Fathima")
courses["Cloud"].remove("Neha")

emp = []
for i in courses:
    print(f"{i} -> {courses[i]}")
    emp.extend(courses[i])
unique_emp = set(emp)
print("Unique employee names: ",unique_emp)

# output

# Python -> ['Arjun', 'Neha', 'Ravi', 'Fathima']
# Java -> ['Vikram', 'Fatima']
# Cloud -> ['Ravi', 'Priya']
# Data Science -> ['Arjun', 'Vikram']
# Unique employee names:  {'Priya', 'Vikram', 'Arjun', 'Fatima', 'Neha', 'Ravi', 'Fathima'}  
