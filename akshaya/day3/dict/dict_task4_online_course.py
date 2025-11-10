# Task 4: Online Course Enrollment Tracker

courses = {
    "Python": ["Arjun", "Neha", "Ravi"],
    "Java": ["Vikram", "Fatima"],
    "Cloud": ["Neha", "Ravi", "Priya"]
}

courses["Data Science"] = ["Arjun", "Vikram"]

courses["Python"].append("Fatima")

courses["Cloud"].remove("Neha")

print("Course Enrollment Details:")
for course, participants in courses.items():
    print(f"{course} → {participants}")

all_employees = set()
for participants in courses.values():
    all_employees.update(participants)

print("\nAll Unique Enrolled Employees:")
print(all_employees)


#sample output
# Course Enrollment Details:
# Python → ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java → ['Vikram', 'Fatima']
# Cloud → ['Ravi', 'Priya']
# Data Science → ['Arjun', 'Vikram']

# All Unique Enrolled Employees:
# {'Fatima', 'Ravi', 'Arjun', 'Priya', 'Neha', 'Vikram'}
