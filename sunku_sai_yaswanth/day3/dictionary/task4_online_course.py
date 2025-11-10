# Task 4: Online Course Enrollment Tracker
# Scenario:
# You are managing course enrollments for UST’s employee learning portal.
# Each course has a name and a set of enrolled employees.
# Instructions:
# 1. Create a dictionary courses :
# courses = {
#  "Python": ["Arjun", "Neha", "Ravi"],
#  "Java": ["Vikram", "Fatima"],
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
 "Java": ["Vikram", "Fatima"],"Cloud": ["Neha", "Ravi", "Priya"]
}
# Add "Data Science": ["Arjun", "Vikram"] .

courses["Data Science"]= {"Arjun", "Vikram"}

#  Remove "Neha" from "Cloud" .

for sub,names in courses.items():
    if sub=="Cloud":
        names.remove("Neha")
        

# . Print all courses and their participants in this format:
for sub,names in courses.items():
    print(f"{sub}---{names}")


# . Print all unique employee names who are enrolled in any course (no
# duplicates).

unique_names=set()
for names in courses.values():
    unique_names.update(names)

print(unique_names)


# output
# Python---['Arjun', 'Neha', 'Ravi']
# Java---['Vikram', 'Fatima']
# Cloud---['Ravi', 'Priya']
# Data Science---{'Arjun', 'Vikram'}
# {'Neha', 'Priya', 'Fatima', 'Ravi', 'Arjun', 'Vikram'}