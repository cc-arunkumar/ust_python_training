# UST INDIA – Employee Data Processing
# Task
# Scenario
# UST HR India collects employee data from different offices:
# Trivandrum
# Kochi
# Bangalore
# Chennai
# Pune
# Hyderabad
# The raw data is stored in a employees_raw.json file.
# However, the data:
# contains missing fields
# contains invalid salaries
# contains wrong phone formats
# contains extra spaces
# contains mixed languages (Indian names)
# contains multiple religions, genders, regions
# contains employees from all over India
# Your task:
# 1. Read the raw JSON
# 2. Validate & clean the data
# JSON 1
# 3. Generate a new clean JSON file employees_cleaned.json
# 4. Generate an error file employees_errors.json

import re
import json
cleaned=[]
errors=[]

#reading the data 
with open("day12/employees_raw.json","r") as employee_data_file:
    reader=json.load(employee_data_file)
data=reader["employees"]
print("Total data: ",len(data))

#headers for validation of missing fields
headers=["emp_id","name","age","salary","department","phone","email"]
for row in data:
    flag=True
    #checking for the qwmissing fields
    if "" in row.values() or None in row.values():
        emp={"emp_id":row["emp_id"],"error_reason":"Missing filed"}
        if emp not in errors:
            errors.append(emp)
        flag=False
    
    #removing the spaces in string
    row["name"]=" ".join(row["name"].split())
    # print(row["name"])
    
    #validating the age
    try:
        if flag:
            row["age"]=int(row["age"])
            if row["age"]<18 or row["age"]>65:
                raise Exception

    except:
        flag=False
        emp={"emp_id":row["emp_id"],"error_reason":"Age is not valid"}
        if emp not in errors:
            errors.append(emp)
    
    #validating the salary
    try: 
        if flag:
            row["salary"]=int(row["salary"])
            if row["salary"]<=0:
                raise Exception
    except:
        flag=False
        emp={"emp_id":row["emp_id"],"error_reason":"Invalid salary"}
        if emp not in errors:
            errors.append(emp)
        
    #validating the phone number
    try:
        if flag:
            if len(row["phone"])!=10:
                raise Exception
            row["phone"]=int(row["phone"])
        
    except:
        flag=False
        emp={"emp_id":row["emp_id"],"error_reason":"Invalid phone number"}
        if emp not in errors:
            errors.append(emp)
        
    #validating the email
    if flag:
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, row["email"]):
            emp={"emp_id":row["emp_id"],"error_reason":"Invalid Email format"}
            if emp not in errors:
                errors.append(emp)
            flag=False
    
    #Cleaned data
    if flag:cleaned.append(row)
    
# print(errors)
print("==========================")
print("Errors List length: ",len(errors))
new_errors={}
new_errors["errors"]=errors
with open("employees_errors.json","w") as file:
    writer=json.dump(new_errors,file,indent=2)

# print(cleaned)
print("==========================")
new_cleaned={}
new_cleaned["cleaned_employees"]=cleaned
print("Cleaned List Length: ",len(cleaned))
with open("employees_cleaned.json","w") as file:
    writer=json.dump(new_cleaned,file,indent=2)
    

# Total data:  50
# ==========================
# Errors List length:  24
# ==========================
# Cleaned List Length:  26