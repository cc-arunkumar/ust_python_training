#Task 4: : Online Course Enrollment Tracker

#Code
courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}
courses["Data Science"]=["Arjun","Vikaram"]
courses["Python"].append("Fatima")
courses["Cloud"].remove("Neha")


for course, participants in courses.items():
    print(f'"{course}": {participants}')

#Output
# "Python": ['Arjun', 'Neha', 'Ravi', 'Fatima']
# "Java": ['Vikram', 'Fatima']
# "Cloud": ['Ravi', 'Priya']
# "Data Science": ['Arjun', 'Vikaram']
