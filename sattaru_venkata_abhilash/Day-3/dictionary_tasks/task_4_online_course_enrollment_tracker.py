# Task 4: Online Course Enrollment Tracker
# Scenario:
# You are managing course enrollments for UST’s employee learning portal.
# Each course has a name and a list of enrolled employees.

# Step 1: Create the dictionary
courses = {
    "Python": ["Arjun", "Neha", "Ravi"],
    "Java": ["Vikram", "Fatima"],
    "Cloud": ["Neha", "Ravi", "Priya"]
}

# Step 2: Add a new course
courses["Data Science"] = ["Arjun", "Vikram"]

# Step 3: Add "Fatima" to the Python course
courses["Python"].append("Fatima")

# Step 4: Remove "Neha" from "Cloud"
courses["Cloud"].remove("Neha")

# Step 5: Print all courses and participants
print("Course Enrollments:")
for course, participants in courses.items():
    print(f"{course} -----> {participants}")

# Step 6: Print all unique employee names (no duplicates)
all_employees = set()
for participants in courses.values():
    all_employees.update(participants)

print("All Unique Employees Enrolled:", all_employees)


# Sample Output:
# Course Enrollments:
# Python -----> ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java -----> ['Vikram', 'Fatima']
# Cloud -----> ['Ravi', 'Priya']
# Data Science -----> ['Arjun', 'Vikram']
# All Unique Employees Enrolled: {'Vikram', 'Ravi', 'Arjun', 'Fatima', 'Neha', 'Priya'}
