#Task 4: Online Course Enrollment Tracker
courses = {"Python": ["Arjun", "Neha", "Ravi"],"Java": ["Vikram", "Fatima"],"Cloud": ["Neha", "Ravi", "Priya"]}
courses["Data Science"]= ["Arjun", "Vikram"]
courses["Python"].append("Fatima")
courses["Cloud"].remove("Neha")

all=set()
for key,value in courses.items():
    print(key,"->",value)
    for j in value:
        all.add(j)
print(all)

# #Sample output
# Python -> ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java -> ['Vikram', 'Fatima']
# Cloud -> ['Ravi', 'Priya']
# Data Science -> ['Arjun', 'Vikram']
# {'Ravi', 'Arjun', 'Neha', 'Priya', 'Fatima', 'Vikram'}