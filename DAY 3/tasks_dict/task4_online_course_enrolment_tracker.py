"""
Task 4: Online Course Enrollment Tracker
Scenario:
You are managing course enrollments for UST’s employee learning portal.
Each course has a name and a set of enrolled employees.

"""

# Dictionary with course names as keys and list of enrolled employees as values
courses={
"Python":["Arjun","Neha","Ravi"],
"Java":["Vikram","Fatima"],
"Cloud":["Neha","Ravi","Priya"]
}

# Add a new course "Data Science" with enrolled employees
courses["Data Science"]=["Arjun","Vikram"]

# Add a new employee to existing course "Python"
courses["Python"].append("Fatima")

# Remove an employee from "Cloud" course
courses["Cloud"].remove("Neha")

# Print each course with its enrolled employees
for c,n in courses.items():
    print(f"{c} → {n}")

# Set to track all unique employees across courses
unique=set()

# Collect all unique employees from all courses
for n in courses.values():
    unique.update(n)

# Print list of all unique employees
print("All Unique Employees:",list(unique))


# sample output

"""
Python → ['Arjun', 'Neha', 'Ravi', 'Fatima']
Java → ['Vikram', 'Fatima']
Cloud → ['Ravi', 'Priya']
Data Science → ['Arjun', 'Vikram']
All Unique Employees: ['Neha', 'Ravi', 'Arjun', 'Fatima', 'Vikram', 'Priya']
"""
