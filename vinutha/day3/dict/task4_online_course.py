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

#Code

# Create a dictionary of courses
# Each course has a list of participants (employees enrolled)
courses = {
    "Python": ["Arjun", "Neha", "Ravi"],
    "Java": ["Vikram", "Fatima"],
    "Cloud": ["Neha", "Ravi", "Priya"]
}

# Add a new course "Data Science" with participants
courses.update({"Data Science": ["Arjun", "Vikram"]})

# Add a new participant "Fatima" to the Python course
courses["Python"].append("Fatima")

# Remove participant "Neha" from the Cloud course
courses["Cloud"].remove("Neha")

# Print all courses with their participants
for course, participants in courses.items():
    print(f"{course} → {participants}")

# Create a set to store unique employees across all courses
unique = set()
for participants in courses.values():
    # Update the set with participants from each course
    unique.update(participants)

# Print the unique employees (no duplicates)
print("Unique Employees:", unique)


#output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task4_online_Course.py
# Python → ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java → ['Vikram', 'Fatima']
# Cloud → ['Ravi', 'Priya']
# Data Science → ['Arjun', 'Vikram']
# Unique Employees: {'Priya', 'Neha', 'Ravi', 'Fatima', 'Arjun', 'Vikram'}
# PS C:\Users\303379\day3_training> 