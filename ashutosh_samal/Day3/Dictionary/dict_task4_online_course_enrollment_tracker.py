#Task 4: Online Course Enrollment Tracker

# Dictionary representing courses and the employees enrolled in each course
courses = {
    "Python": ["Arjun", "Neha", "Ravi"],
    "Java": ["Vikram", "Fatima"],
    "Cloud": ["Neha", "Ravi", "Priya"]
}

# Adding a new course "Data Science" with the employees enrolled
courses["Data Science"] = ["Arjun", "Vikram"]

# Appending a new student ("Fatima") to the "Python" course
courses["Python"].append("Fatima")

# Removing a student ("Neha") from the "Cloud" course
courses["Cloud"].remove("Neha")

# Printing each course with the list of enrolled employees
for name, employee in courses.items():
    print(f"{name} : {employee}")

# Creating a set to hold all unique employees across all courses
unique_employee = set()

# Looping through all course lists and adding employees to the set
for i in courses.values():
    unique_employee.update(i)

# Printing the set of unique employees across all courses
print(unique_employee)



#Sample Execution
# Python : ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java : ['Vikram', 'Fatima']
# Cloud : ['Ravi', 'Priya']
# Data Science : ['Arjun', 'Vikram']
# {'Arjun', 'Vikram', 'Ravi', 'Priya', 'Neha', 'Fatima'}