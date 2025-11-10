#online_course_enrollment_tracker
# You are managing course enrollments for UST’s employee learning portal.
# Each course has a name and a set of enrolled employees.

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


#Sample output

# Added Data science: {'Python': ['Arjun', 'Neha', 'Ravi'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Neha', 'Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# Added Fatima and removed Neha {'Python': ['Arjun', 'Neha', 'Ravi', 'Fatima'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# Python-->['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java-->['Vikram', 'Fatima']
# Cloud-->['Ravi', 'Priya']
# Data Science-->['Arjun', 'Vikram']
# Unique Employee names: {'Neha', 'Priya', 'Ravi', 'Arjun', 'Fatima', 'Vikram'}