# Task 3: Department Budget Tracker (Nested Dictionary)

# Scenario:
# The Finance team maintains a yearly budget tracker for each department.

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
departments["Operations"]={"manager":"Vikram", "budget": 35}
# print(departments)
# for dep, val in departments.items():
#     if dep=="Finance":
#         for mgr, bgt in val.items():
#             val[bgt]=45
# print(departments)
for dep, val in departments.items():
    if dep == "Finance":
        val["budget"] = 45

print(departments["IT"]["manager"])


for dept, value in departments.items():
     if dept == "IT":
         
        print("IT's Manager Name:", value["manager"])
total_budget = sum(info["budget"] for info in departments.values())
print("Total Company Budget:", total_budget, "Lakhs")

#Sample Output
# Arjun
# IT's Manager Name: Arjun
# Total Company Budget: 155 Lakhs