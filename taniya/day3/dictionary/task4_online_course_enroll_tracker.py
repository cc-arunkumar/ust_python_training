# Dictionary of courses with participants
courses = {
    "Python": ["Arjun", "Neha", "Ravi"],
    "Java": ["Vikram", "Fatima"],
    "Cloud": ["Neha", "Ravi", "Priya"]
}

# Add a new course with participants
courses["Data Science"] = ["Arjun", "Vikram"]

# Print dictionary after adding new course
print(courses)

# Add a new participant to Python course
courses["Python"].append("Fatima")

# Remove a participant from Cloud course
courses["Cloud"].remove("Neha")

# Print dictionary after modifications
print(courses)

# Print all courses with their participants
for course, participants in courses.items():
    print(f"{course} → {participants}")

# Collect all unique employee names across courses
unique_names = set()
for participants in courses.values():
    unique_names.update(participants)

# Print unique employees list
print("Unique Employees:", list(unique_names))

# -------------------------
# Expected Output:
# {'Python': ['Arjun', 'Neha', 'Ravi'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Neha', 'Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# {'Python': ['Arjun', 'Neha', 'Ravi', 'Fatima'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# Python → ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java → ['Vikram', 'Fatima']
# Cloud → ['Ravi', 'Priya']
# Data Science → ['Arjun', 'Vikram']
# Unique Employees: ['Fatima', 'Ravi', 'Arjun', 'Priya', 'Neha', 'Vikram']