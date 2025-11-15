# Task 4: Online Course Enrollment Tracker
# Scenario:
# You are managing course enrollments for UST’s employee learning portal.
# Each course has a name and a set of enrolled employees.
# Instructions:
# 1. Create a dictionary courses :
# courses = {
#  "Python": ["Arjun", "Neha", "Ravi"],
#  "Java": ["Vikram", "Fatima"],
# Dictionary Tasks 3
#  "Cloud": ["Neha", "Ravi", "Priya"]
# }
# 2. Add "Data Science": ["Arjun", "Vikram"] .
# 3. Add "Fatima" to the "Python" course list.
# 4. Remove "Neha" from "Cloud" .
# 5. Print all courses and their participants in this format:
# Python → ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java → ['Vikram', 'Fatima']
# 6. Print all unique employee names who are enrolled in any course (no
# duplicates).

courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
"Cloud": ["Neha", "Ravi", "Priya"]
}
# Add Data Science course
courses["Data Science"]=["Arjun", "Vikram"]

# Add Fatima to Python course
courses["Python"].append("Fatima")

# Remove Neha from Cloud course
courses["Cloud"].remove("Neha")

# Print all courses and their participants
for dept,name in courses.items():
    print(f"{dept} ->{name}")

# Print all unique employee names
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



