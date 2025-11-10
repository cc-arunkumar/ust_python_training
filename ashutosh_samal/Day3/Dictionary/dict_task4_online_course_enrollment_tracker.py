#Task 4: Online Course Enrollment Tracker

courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}

courses["Data Science"]=["Arjun","Vikram"]
courses["Python"].append("Fatima")
courses["Cloud"].remove("Neha")

for name,employee in courses.items():
    print(f"{name} : {employee}")

unique_employee=set()
for i in courses.values():
    unique_employee.update(i)

print(unique_employee)


#Sample Execution
# Python : ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java : ['Vikram', 'Fatima']
# Cloud : ['Ravi', 'Priya']
# Data Science : ['Arjun', 'Vikram']
# {'Arjun', 'Vikram', 'Ravi', 'Priya', 'Neha', 'Fatima'}