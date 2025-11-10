courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}
courses["Data Science"] = ["Arjun", "Vikram"]
print(courses)

courses["Python"] = ["Arjun", "Neha", "Ravi","Fatima"]
print(courses)
courses["Cloud"]=["Ravi", "Priya"]
print(courses)

for item in courses:
    print(f"{item}-> {courses[item]}")

unique = set()
for items in courses.values():
    unique.update(items)
print(unique)

# ======sample output===================
# Cloud-> ['Ravi', 'Priya']
# Data Science-> ['Arjun', 'Vikram']
# {'Vikram', 'Priya', 'Neha', 'Fatima', 'Arjun', 'Ravi'}