# Task 4: Online Course Enrollment Tracker

# Scenario:
# You are managing course enrollments for UST’s employee learning portal.
# Each course has a name and a set of enrolled employees.

# Instructions:
# 1. Create a dictionary courses :
# courses = {
#  "Python": ["Arjun", "Neha", "Ravi"],
#  "Java": ["Vikram", "Fatima"],
# Dictionary Tasks 3
#  "Cloud": ["Neha", "Ravi", "Priya"]
# }
# 2. Add "Data Science": ["Arjun", "Vikram"] .
# 3. Add "Fatima" to the "Python" course list.
# 4. Remove "Neha" from "Cloud" .
# 5. Print all courses and their participants in this format:
# Python → ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java → ['Vikram', 'Fatima']
# 6. Print all unique employee names who are enrolled in any course (no
# duplicates).


courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}

print("Before editing the cources:", courses)

courses["Data Science"] =["Arjun", "Vikram"]

print("After adding data science to cources:",courses)

courses["Python"].append("Fatima")

print("After adding to python:", courses)

courses["Cloud"].remove("Neha")

print("After deleting in cloud:", courses)

for key,val in courses.items():
    print(f"{key}-> {val}")

# Sample output

# Before editing the cources: {'Python': ['Arjun', 'Neha', 'Ravi'], 
# 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Neha', 'Ravi', 'Priya']}

# After adding data science to cources: {'Python': ['Arjun', 'Neha', 'Ravi'], 
# 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Neha', 'Ravi', 'Priya'], 
# 'Data Science': ['Arjun', 'Vikram']}

# After adding to python: {'Python': ['Arjun', 'Neha', 'Ravi', 'Fatima'], 
# 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Neha', 'Ravi', 'Priya'], 
# 'Data Science': ['Arjun', 'Vikram']}

# After deleting in cloud: {'Python': ['Arjun', 'Neha', 'Ravi', 'Fatima'], 
# 'Java': ['Vikram', 'Fatima'], 'Cloud': ['Ravi', 'Priya'], 
# 'Data Science': ['Arjun', 'Vikram']}

# Python-> ['Arjun', 'Neha', 'Ravi', 'Fatima']
# Java-> ['Vikram', 'Fatima']
# Cloud-> ['Ravi', 'Priya']
# Data Science-> ['Arjun', 'Vikram']