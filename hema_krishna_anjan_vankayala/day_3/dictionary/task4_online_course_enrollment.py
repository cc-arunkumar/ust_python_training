#Task 4: Online Course Enrollment Tracker

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

courses["Data Science"] = ["Arjun","Vikram"]
courses["Python"].append("Fathima")
courses["Cloud"].remove("Neha")

unique_employees=set()
for course in list(courses.items()):
    for i in course[1]:
        unique_employees.add(i)
    print(f"{course[0]} -> {course[1]}")

print("Unique Employees",unique_employees)

#Sample Output
# Python -> ['Arjun', 'Neha', 'Ravi', 'Fathima']
# Java -> ['Vikram', 'Fatima']
# Cloud -> ['Ravi', 'Priya']
# Data Science -> ['Arjun', 'Vikram']
# Unique Employees {'Ravi', 'Neha', 'Vikram', 'Fatima', 'Priya', 'Fathima', 'Arjun'}