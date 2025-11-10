departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}
# add "Operations": {"manager": "Vikram", "budget": 35} .
departments["Operations"]={"manager": "Vikram", "budget": 35}
print(departments)


for dept,val in departments.items():
    if dept=="Finance":
        for k, v in val.items():
            if k == "budget":
                val[k] = 45
print(departments)
                


# Print IT’s manager name.

for dept,val in departments.items():
    if dept=="IT":
        for k,v in val.items():
            if k=="manager":
                print(v)


# Print each department:
# "Operations": {"manager": "Vikram", "budget": 35} .
for dept,val in departments.items():
    for k,v in val.items():
        if k == "manager":
            print(f"Department: {dept} | Manager: {v} | Budget: {val["budget"]} Lakhs ")



# Display total company budget (sum of all budgets).

sum=0
for dept,val in departments.items():
    for k,v in val.items():
        if k=="budget":
            sum+=v
print(sum)




# =============sample Execution==============
# {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 40}, 'Operations': {'manager': 'Vikram', 'budget': 35}}
# {'HR': {'manager': 'Neha', 'budget': 25}, 'IT': {'manager': 'Arjun', 'budget': 50}, 'Finance': {'manager': 'Fatima', 'budget': 45}, 'Operations': {'manager': 'Vikram', 'budget': 35}}
# Arjun
# Department: HR | Manager: Neha | Budget: 25 Lakhs
# Department: IT | Manager: Arjun | Budget: 50 Lakhs
# Department: Finance | Manager: Fatima | Budget: 45 Lakhs
# Department: Operations | Manager: Vikram | Budget: 35 Lakhs
# 155





     
