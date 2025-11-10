courses = {
    "Python": ["Arjun", "Neha", "Ravi"],
    "Java": ["Vikram", "Fatima"],
    "Cloud": ["Neha", "Ravi", "Priya"]
}


courses["Data Science"] = ["Arjun", "Vikram"]


courses["Python"].append("Fatima")


if "Neha" in courses["Cloud"]:
    courses["Cloud"].remove("Neha")


for course, participants in courses.items():
    print(f"{course} → {participants}")


unique_participants = set()
for participants in courses.values():
    unique_participants.update(participants)


