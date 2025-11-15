#online_course_enrollment_tracker
# You are managing course enrollments for UST’s employee learning portal.
# Each course has a name and a set of enrolled employees.
# Dictionary storing courses and their enrolled students
courses = {
    "Python": ["Arjun", "Neha", "Ravi"],
    "Java": ["Vikram", "Fatima"],
    "Cloud": ["Neha", "Ravi", "Priya"]
}

# Add a new course with enrolled students
courses["Data Science"] = ["Arjun", "Vikram"]
print("Added Data Science:", courses)

# Modify the courses:
# Add "Fatima" to the Python course
# Remove "Neha" from the Cloud course
for key, val in courses.items():
    if key == "Python":
        courses[key].append("Fatima")
    if key == "Cloud":
        courses[key].remove("Neha")

# Print the updated courses after modifications
print("Added Fatima and removed Neha", courses)

# Print the courses and their enrolled students
for key, val in courses.items():
    print(f"{key} --> {val}")

# Create a set to store unique student names across all courses
un = set()

# Update the set with all unique student names from the courses
for i in courses.values():
    un.update(i)

# Print the unique student names
print("Unique Employee names:", un)



#Sample output

# Added Data science: {'Python': ['Arjun', 'Neha', 'Ravi'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Neha', 'Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# Added Fatima and removed Neha {'Python': ['Arjun', 'Neha', 'Ravi', 'Fatima'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# Python-->['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java-->['Vikram', 'Fatima']
# Cloud-->['Ravi', 'Priya']
# Data Science-->['Arjun', 'Vikram']
# Unique Employee names: {'Neha', 'Priya', 'Ravi', 'Arjun', 'Fatima', 'Vikram'}