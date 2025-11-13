# Task 4: Online Course Enrollment Tracker
courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],"Cloud": ["Neha", "Ravi", "Priya"]
}
# Add "Data Science": ["Arjun", "Vikram"] .

courses["Data Science"]= {"Arjun", "Vikram"}

#  Remove "Neha" from "Cloud" .

for sub,names in courses.items():
    if sub=="Cloud":
        names.remove("Neha")
        

# . Print all courses and their participants in this format:
for sub,names in courses.items():
    print(f"{sub}---{names}")


# . Print all unique employee names who are enrolled in any course (no
# duplicates).

unique_names=set()
for names in courses.values():
    unique_names.update(names)

print(unique_names)


# output
# Python---['Arjun', 'Neha', 'Ravi']
# Java---['Vikram', 'Fatima']
# Cloud---['Ravi', 'Priya']
# Data Science---{'Arjun', 'Vikram'}
# {'Neha', 'Priya', 'Fatima', 'Ravi', 'Arjun', 'Vikram'}