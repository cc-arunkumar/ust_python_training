# Task 3: Department Budget Tracker
# (Nested Dictionary)
# Scenario:
# The Finance team maintains a yearly budget tracker for each department
# Instructions:
# 1. Create a nested dictionary:
# departments = {
#  "HR": {"manager": "Neha", "budget": 25},
#  "IT": {"manager": "Arjun", "budget": 50},
#  "Finance": {"manager": "Fatima", "budget": 40}
# }
# 2. Add "Operations": {"manager": "Vikram", "budget": 35} .
# 3. Update Finance budget → 45 .
# 4. Print IT’s manager name.
# 5. Print each department:
# Department: HR | Manager: Neha | Budget: 25 Lakhs
# 6. Display total company budget (sum of all budgets).
departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}

# Update Finance budget → 45 .

departments ["Operations"]= {"manager": "Vikram", "budget": 35}

for dept, team in departments.items():
    if dept=="Finance":
        for k,v in team.items():
            team["budget"]=45
print("after update of finance budget:",departments)


#  Print IT’s manager name.

for dept,team in departments.items():
    if dept=="IT":
        print("Manager name is:",team["manager"])

#  Print each department:
for dept,team in departments.items():
    print(f"Department:{dept}|manager:{team["manager"]}|Budget:{team["budget"]}")

sum=0
for dept,team in departments.items():
    sum+=team["budget"]
print(f"sum of budgets:{sum}")

# output
# after update of finance budget: {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 45}, 'Operations': {'manager': 'Vikram', 'budget': 35}}
# Manager name is: Arjun
# Department:HR|manager:Neha|Budget:25
# Department:IT|manager:Arjun|Budget:50
# Department:Finance|manager:Fatima|Budget:45
# Department:Operations|manager:Vikram|Budget:35
# sum of budgets:155





