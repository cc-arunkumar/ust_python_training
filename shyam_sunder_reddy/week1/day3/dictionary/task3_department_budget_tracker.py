# #Task 3: Department Budget Tracker(Nested Dictionary)
# Scenario:
# The Finance team maintains a yearly budget tracker for each department.
# Dictionary Tasks 2
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
# # Department: HR | Manager: Neha | Budget: 25 Lakhs
# 6. Display total company budget (sum of all budgets)

departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}

departments["Operations"]= {"manager": "Vikram", "budget": 35}
x=departments["Finance"]
x["budget"]=45

print(departments["IT"]["manager"])

sum=0
for key,value in departments.items():
    print("Department: ",key,end="|")
    for i,j in value.items():
        if isinstance(j, int):
            sum=sum+j
            print(i,":",j,"Lakhs")
        else:
            print(i,":",j,end=" | ")
print("Toatal Budget",sum)

#Sample output
# Arjun
# Department:  HR|manager : Neha | budget : 25 Lakhs
# Department:  IT|manager : Arjun | budget : 50 Lakhs
# Department:  Finance|manager : Fatima | budget : 45 Lakhs
# Department:  Operations|manager : Vikram | budget : 35 Lakhs
# Toatal Budget 155