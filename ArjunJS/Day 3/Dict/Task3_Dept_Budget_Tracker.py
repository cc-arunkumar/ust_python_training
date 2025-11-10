#Task 3: Department Budget Tracker(Nested Dictionary)
departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}

departments["Operations"]= {"manager": "Vikram", "budget": 35}
departments["Finance"]["budget"]=45
print(f"IT Manager name : {departments["IT"]["manager"]}")
buget_tot=0
for i in departments:
    buget_tot+=departments.get(i)["budget"]
    print(f"Department: {i} | Manager: {departments.get(i)["manager"]} | Budget: {departments.get(i)["budget"]} Lakhs")

print(f"Total budget : {buget_tot}")
#Output
# IT Manager name : Arjun
# Department: HR | Manager: Neha | Budget: 25 Lakhs
# Department: IT | Manager: Arjun | Budget: 50 Lakhs
# Department: Finance | Manager: Fatima | Budget: 45 Lakhs
# Department: Operations | Manager: Vikram | Budget: 35 Lakhs
# Total budget : 155