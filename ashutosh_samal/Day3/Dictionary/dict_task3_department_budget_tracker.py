#Task 3: Department Budget Tracker

departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}

departments["Operations"] = {"manager": "Vikram","budget":35}

departments["Finance"]["budget"] = 45

print("IT's manager name:",departments["IT"]["manager"])

sum=0
for dept,info in departments.items():
    print(f"Department: {dept} | Manager: {info['manager']} | Budget: {info['budget']}")

    sum=sum+info['budget']

print("Total company budget: ",sum)


#Sample Execution
# IT's manager name: Arjun
# Department: HR | Manager: Neha | Budget: 25
# Department: IT | Manager: Arjun | Budget: 50
# Department: Finance | Manager: Fatima | Budget: 45
# Department: Operations | Manager: Vikram | Budget: 35
# Total company budget:  155