courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}
courses["Data Science"]=["Arjun", "Vikram"]
print("Added Data science:",courses)
for key,val in courses.items():
    if key=="Python":
        courses[key].append("Fatima")
    if key=="Cloud":
        courses[key].remove("Neha")
print("Added Fatima and removed Neha",courses)
for key,val in courses.items():
    print(f"{key}-->{val}")
un=set()
for i in courses.values():
    un.update(i)
print("Unique Employee names:",un)


# Added Data science: {'Python': ['Arjun', 'Neha', 'Ravi'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Neha', 'Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# Added Fatima and removed Neha {'Python': ['Arjun', 'Neha', 'Ravi', 'Fatima'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# Python-->['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java-->['Vikram', 'Fatima']
# Cloud-->['Ravi', 'Priya']
# Data Science-->['Arjun', 'Vikram']
# Unique Employee names: {'Neha', 'Priya', 'Ravi', 'Arjun', 'Fatima', 'Vikram'}