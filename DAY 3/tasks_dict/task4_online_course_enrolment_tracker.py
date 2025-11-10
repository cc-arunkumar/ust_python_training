"""
Task 4: Online Course Enrollment Tracker
Scenario:
You are managing course enrollments for UST’s employee learning portal.
Each course has a name and a set of enrolled employees.

"""


courses={
"Python":["Arjun","Neha","Ravi"],
"Java":["Vikram","Fatima"],
"Cloud":["Neha","Ravi","Priya"]
}
courses["Data Science"]=["Arjun","Vikram"]
courses["Python"].append("Fatima")
courses["Cloud"].remove("Neha")

for c,n in courses.items():
    print(f"{c} → {n}")
unique=set()

for n in courses.values():
    unique.update(n)

print("All Unique Employees:",list(unique))


# sample output

"""
Python → ['Arjun', 'Neha', 'Ravi', 'Fatima']
Java → ['Vikram', 'Fatima']
Cloud → ['Ravi', 'Priya']
Data Science → ['Arjun', 'Vikram']
All Unique Employees: ['Neha', 'Ravi', 'Arjun', 'Fatima', 'Vikram', 'Priya']
"""