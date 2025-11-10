#Task 4: Online Course Enrollment Tracker
courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}
courses["Data Science"]= ["Arjun", "Vikram"]
courses["Python"].append("Fathima")
courses["Cloud"].remove("Neha")
L=[]
for i in courses:
    print(f"{i}->{courses.get(i)}")
    for j in courses.get(i):
        if(j not in L):
            L.append(j)
print(f"Unique Students : {L}")
#Output
# Python->['Arjun', 'Neha', 'Ravi', 'Fathima']
# Java->['Vikram', 'Fatima']
# Cloud->['Ravi', 'Priya']
# Data Science->['Arjun', 'Vikram']
# Unique Students : ['Arjun', 'Neha', 'Ravi', 'Fathima', 'Vikram', 'Fatima', 'Priya']