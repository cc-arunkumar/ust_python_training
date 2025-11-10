# Online_Course_Enrollment_Tracker

courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}
courses["Data Science"]= ["Arjun", "Vikram"]
courses["Python"].append("Fatima")
courses["Cloud"].remove("Neha")
uniq=set()
for i in courses:
    print(f"{i} -> {courses[i]}")
    uniq.update(courses[i])

print("unique employee names who are enrolled in any course: ",uniq)

# Python -> ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java -> ['Vikram', 'Fatima']
# Cloud -> ['Ravi', 'Priya']
# Data Science -> ['Arjun', 'Vikram']
# unique employee names who are enrolled in any course:  {'Ravi', 'Fatima', 'Arjun', 'Neha', 'Vikram', 'Priya'}