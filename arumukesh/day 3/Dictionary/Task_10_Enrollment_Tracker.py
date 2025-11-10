courses = { "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],"Cloud": ["Neha", "Ravi", "Priya"]}
print("Adding new course")
courses["Data Science"]=["Arjun", "Vikram"]
print("Updated Courses:",courses)
print("Enrolling Fatima to Python course")
courses["Python"].append("Fatima")
print("Updated Courses:",courses)
print("Removing Neha from Cloud course")
courses["Cloud"].remove("Neha")
print("Updated Courses:",courses)
for course in courses:
    print(f"Course:{course} Enrolled Students:{len(courses[course])}")
list_courses=[]
for course in courses:
    list_courses.extend(courses[course])
print("Unique Names:",set(list_courses))


# Adding new course
# Updated Courses: {'Python': ['Arjun', 'Neha', 'Ravi'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Neha', 'Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# Enrolling Fatima to Python course
# Updated Courses: {'Python': ['Arjun', 'Neha', 'Ravi', 'Fatima'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Neha', 'Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# Removing Neha from Cloud course
# Updated Courses: {'Python': ['Arjun', 'Neha', 'Ravi', 'Fatima'], 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Ravi', 'Priya'], 'Data Science': ['Arjun', 'Vikram']}
# Course:Python Enrolled Students:4
# Course:Java Enrolled Students:2
# Course:Cloud Enrolled Students:2
# Course:Data Science Enrolled Students:2
# Unique Names: {'Vikram', 'Ravi', 'Neha', 'Arjun', 'Priya', 'Fatima'}