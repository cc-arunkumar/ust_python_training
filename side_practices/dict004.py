departments = {
 "HR": {"manager": "Neha", "budget": 25},
 "IT": {"manager": "Arjun", "budget": 50},
 "Finance": {"manager": "Fatima", "budget": 40}
}

tot_com_bud = 0

departments["Operations"] =  {"manager": "Vikram", "budget": 35}

#departments.update({"Finance":{"manager":"Fatima","budget":45}}) #Updating a dictionary

departments["Finance"]["budget"] = 45 #This way also

for key,details in departments.items():
    print(f"Department:{key} | Manager:{details["manager"]} | Budget:{details["budget"]}")
    tot_com_bud += details["budget"]

print(tot_com_bud)



