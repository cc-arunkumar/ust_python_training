departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}
departments["Operations"]={"manager": "Vikram", "budget": 35}
print("updated departments:",departments)
# for item in departments:
    # if item=="Finance":
        # for k in item:
departments["Finance"]["budget"]=45
print("updated department:",departments)
print("IT Mangaer:",departments["IT"]["manager"])
print("All departments:",departments.keys())
tot=0
for item in departments:
    tot+=departments[item]["budget"]
# print("Total Budget:",tot)
# updated departments: {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 40}, 'Operations': {'manager': 'Vikram', 'budget': 35}}
# updated department: {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 45}, 'Operations': {'manager': 'Vikram', 'budget': 35}}
# IT Mangaer: Arjun
# All departments: dict_keys(['HR', 'IT', 'Finance', 'Operations'])
# Total Budget: 155