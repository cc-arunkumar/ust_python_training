import csv
employees=[ 
    {"id":201,"name":"suresh","department":"sales","salary":58000},
    {"id":202,"name":"meena","department":"IT","salary":72000},
    {"id":203,"name":"amit","department":"HR","salary":64000}
]

#step-1: create or open CSV file in write mode
with open('employee_dict_data.csv',mode='w',newline='') as file:
    
    #step-2: create the filenmaes
    header=["id","name","department","salary"]
    
    #step-3: create aDictwriter object
    writer=csv.DictWriter(file, fieldnames=header)
    
    #step-4: write the header to the csv
    writer.writeheader()
    
    #step-5: write the employee data to the csv file
    writer.writerows(employees)
    
print("===CSV writing with Dictionary completed===")

#o/p:
# ===CSV writing with Dictionary completed===