#Task 3: Department Budget Tracker(Nested Dictionary)
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