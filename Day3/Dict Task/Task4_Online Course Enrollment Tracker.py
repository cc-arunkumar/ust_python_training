courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
"Cloud": ["Neha", "Ravi", "Priya"]
}

courses["Data Science"]=["Arjun", "Vikram"]
courses["Python"].append("Fatima")
courses["Cloud"].remove("Neha")
for dept,name in courses.items():
    print(f"{dept} ->{name}")

unique_names = set()
for participants in courses.values():
    unique_names.update(participants)

print("\nUnique Employees:", unique_names)

# Python ->['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java ->['Vikram', 'Fatima']
# Cloud ->['Ravi', 'Priya']
# Data Science ->['Arjun', 'Vikram']
#
# Unique Employees: {'Ravi', 'Fatima', 'Priya', 'Arjun', 'Neha', 'Vikram'}



