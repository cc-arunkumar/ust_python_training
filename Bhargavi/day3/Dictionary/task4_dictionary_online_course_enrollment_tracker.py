# Online Course Enrollment Tracker

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


# Dictionary of courses with participants
courses = {
    "Python": ["Arjun", "Neha", "Ravi"],
    "Java": ["Vikram", "Fatima"],
    "Cloud": ["Neha", "Ravi", "Priya"]
}

# Add a new course with participants
courses["Data Science "] = ["Arjun", "Vikram"]

# Update Python course by adding a new participant
courses["Python"].append("Fatima")

# Remove a participant from Cloud course
courses["Cloud"].remove("Neha")

# Print all courses with their participants
for course, participants in courses.items():
    print(f"{course} -> {participants}")

# Collect all unique employee names across courses
unique_employees = set()
for participants in courses.values():
    unique_employees.update(participants)

# Print sorted list of unique employee names
print("\nUnique employee names:", sorted(unique_employees))


#  Output:


# Python -> ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java -> ['Vikram', 'Fatima']
# Cloud -> ['Ravi', 'Priya']
# Data Science  -> ['Arjun', 'Vikram']

# Unique employee names: ['Arjun', 'Fatima', 'Neha', 'Priya', 'Ravi', 'Vikram']