# Online Course Enrollment Tracker
courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}

courses["Data Science "] = ["Arjun" ,"Vikram"]

courses["Python"].append("Fatima")

courses["Cloud"].remove("Neha")

for course, participants in courses.items():
    print(f"{course} -> {participants}")

unique_employees = set()
for participants in courses.values():
    unique_employees.update(participants)

print("\nUnique employee names:", sorted(unique_employees))

# Python -> ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java -> ['Vikram', 'Fatima']
# Cloud -> ['Ravi', 'Priya']
# Data Science  -> ['Arjun', 'Vikram']

# Unique employee names: ['Arjun', 'Fatima', 'Neha', 'Priya', 'Ravi', 'Vikram']