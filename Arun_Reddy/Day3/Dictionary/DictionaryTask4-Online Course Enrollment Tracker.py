courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}

courses[ "Data Science"]= ["Arjun", "Vikram"] 
print(courses)

courses["Python"].append("Fatima")
print(courses)
courses["Cloud"].remove("Neha")
print(courses)


for key,val in courses.items():
    print(f"{key}->{val}")

emp=set()
for key,val in courses.items():
    for item in val:
        emp.add(item)
print(emp)
# =====smaple execution=======
# {'Python': ['Arjun', 'Neha', 'Ravi'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Neha', 'Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# {'Python': ['Arjun', 'Neha', 'Ravi', 'Fatima'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Neha', 'Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# {'Python': ['Arjun', 'Neha', 'Ravi', 'Fatima'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# Python->['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java->['Vikram', 'Fatima']
# Cloud->['Ravi', 'Priya']
# Data Science->['Arjun', 'Vikram']
# {'Fatima', 'Arjun', 'Priya', 'Vikram', 'Neha', 'Ravi'}