#Task 4: Course Enrollment
courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}

courses["Data Science"]=["Arjun","Vikram"]
courses["Python"]=["Arjun","Neha","Ravi","Fatima"]

for course, participants in courses.items():
    print(f"{course} → {participants}")

unique_names=set()
for name in courses.values():
    unique_names.update(name)
print("All unique Employees are:")
print(courses)

'''
output:
Python → ['Arjun', 'Neha', 'Ravi', 'Fatima']
Java → ['Vikram', 'Fatima']
Cloud → ['Neha', 'Ravi', 'Priya']
Data Science → ['Arjun', 'Vikram']

All unique Employees are:
{'Python': ['Arjun', 'Neha', 'Ravi', 'Fatima'], 
'Java': ['Vikram', 'Fatima'], 
'Cloud': ['Neha', 'Ravi', 'Priya'], 
'Data Science': ['Arjun', 'Vikram']}

'''