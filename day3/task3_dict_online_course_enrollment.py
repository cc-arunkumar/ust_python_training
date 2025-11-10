#online course enrollment


courses = {
    "Python": ["Arjun", "Neha", "Ravi"],
    "Java": ["Vikram", "Fatima"],
    "Cloud": ["Neha", "Ravi", "Priya"]
}
courses["Data Science"] = ["Arjun", "Vikram"]
courses["Python"].append("Fatima")
if "Neha" in courses["Cloud"]:
    courses["Cloud"].remove("Neha")
print("Course Enrollments:")
for course, participants in courses.items():
    print(f"{course} → {participants}")
unique_employees = set()
for participants in courses.values():
    unique_employees.update(participants)
print("\nUnique employees enrolled in any course:")
print(sorted(unique_employees))



# output
# Course Enrollments:
# Python → ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java → ['Vikram', 'Fatima']
# Cloud → ['Ravi', 'Priya']
# Data Science → ['Arjun', 'Vikram']

# Unique employees enrolled in any course:
# ['Arjun', 'Fatima', 'Neha', 'Priya', 'Ravi', 'Vikram']