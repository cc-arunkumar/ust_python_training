courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}

courses["Data Science"] =["Arjun", "Vikram"]

print(courses)
courses["Python"].append("Fatima")
print("After adding to python:", courses)

courses["Cloud"].remove("Neha")
print("After deleting in cloud:", courses)

for key,val in courses.items():
    print(f"{key}-> {val}")