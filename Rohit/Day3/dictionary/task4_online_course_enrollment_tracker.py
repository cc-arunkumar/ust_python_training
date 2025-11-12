# Task 4: Online Course Enrollment Tracker
# Scenario:
# You are managing course enrollments for UST’s employee learning portal.
# Each course has a name and a set of enrolled employees


# Step 1: Initialize the courses dictionary with course names as keys and student lists as values
courses = {
    "Python": ["Arjun", "Neha", "Ravi"],
    "Java": ["Vikram", "Fatima"],
    "Cloud": ["Neha", "Ravi", "Priya"]
}

# Step 2: Add a new course with enrolled students
courses["Data Science"] = ["Arjun", "Vikram"]


# Step 4: Update the Python course to include an additional student
courses["Python"] = ["Arjun", "Neha", "Ravi", "Fatima"]

# Step 5: Update the Cloud course to remove one student
courses["Cloud"] = ["Ravi", "Priya"]

# Step 6: Print the final state of the courses dictionary
print("The final state of the courses dictionary")
print(courses)

# Step 7: Display each course and its enrolled students

print("Display each course and its enrolled students")
for item in courses:
    print(f"{item} -> {courses[item]}")

# Step 8: Collect all unique student names across all courses
unique = set()
for items in courses.values():
    unique.update(items)

# Step 9: Print the set of unique student names
print("the set of unique student names")
print(unique)


# ======sample output===================
#The final state of the courses dictionary
# {'Python': ['Arjun', 'Neha', 'Ravi', 'Fatima'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# Display each course and its enrolled students
# Python -> ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java -> ['Vikram', 'Fatima']
# Cloud -> ['Ravi', 'Priya']
# Data Science -> ['Arjun', 'Vikram']

# the set of unique student names
# {'Fatima', 'Neha', 'Ravi', 'Arjun', 'Vikram', 'Priya'}