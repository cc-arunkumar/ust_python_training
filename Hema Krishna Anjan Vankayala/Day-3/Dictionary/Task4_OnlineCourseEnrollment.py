#Task 4: Online Course Enrollment Tracker
courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}

courses["Data Science"] = ["Arjun","Vikram"]
courses["Python"].append("Fathima")
courses["Cloud"].remove("Neha")

unique_employees=set()
for course in list(courses.items()):
    for i in course[1]:
        unique_employees.add(i)
    print(f"{course[0]} -> {course[1]}")

print("Unique Employees",unique_employees)

#Sample Output
# Python -> ['Arjun', 'Neha', 'Ravi', 'Fathima']
# Java -> ['Vikram', 'Fatima']
# Cloud -> ['Ravi', 'Priya']
# Data Science -> ['Arjun', 'Vikram']
# Unique Employees {'Ravi', 'Neha', 'Vikram', 'Fatima', 'Priya', 'Fathima', 'Arjun'}