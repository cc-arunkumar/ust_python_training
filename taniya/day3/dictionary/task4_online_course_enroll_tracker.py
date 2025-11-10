courses = {
 "Python": ["Arjun", "Neha", "Ravi"],
 "Java": ["Vikram", "Fatima"],
 "Cloud": ["Neha", "Ravi", "Priya"]
}
courses["Data Science"] = ["Arjun","Vikram"]
print(courses)
courses["Python"].append("Fatima")
courses["Cloud"].remove("Neha")
print(courses)
for course, participants in courses.items():
    print(f"{course} → {participants}")


unique_names = set()
for participants in courses.values():
    unique_names.update(participants)

print("Unique Employees:", list(unique_names))

