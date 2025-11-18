# UST INDIA – Employee Data Processing Task

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
# 3. Generate a new clean JSON file employees_cleaned.json
# 4. Generate an error file employees_errors.json
import json, re
required_fields = ['emp_id','name','age','salary','department','phone','email']
headers= ['emp_id', 'name', 'age', 'gender', 'city', 'state', 'department', 'salary', 'phone', 'email', 'languages', 'is_active']
errors_list = []
cleaned_list = []
flag = False
with open('employees_raw1.json','r') as file:
    reader = json.load(file)
employees_data = reader['employees']
print(len(employees_data))
for emp in employees_data:
    #check for the missing req fields
    if '' in emp.values():
        err_emp = {"emp_id":emp[headers[0]],"error_reason":"Required Field is Missing"}
        errors_list.append(err_emp)
        continue
        
    # for h in required_fields:
    #     if type(emp[h])!=type(1) and (emp[h] is None or emp[h].strip()==""):
    #         err_emp = {"emp_id":emp[headers[0]],"error_reason":"Required Field is Missing"}
    #         errors_list.append(err_emp)

    
    #name spaces normalization
    name_words = ' '.join(emp[headers[1]].split())
    
    #age validation
    try:
        emp[headers[2]] = int(emp[headers[2]])
        if  not (emp[headers[2]] > 18 and emp[headers[2]]<65):
            err_emp = {"emp_id":emp[headers[0]],"error_reason":"Age should be between 18 and 65"}
            errors_list.append(err_emp)
            continue
    except Exception:
        err_emp = {"emp_id":emp[headers[0]],"error_reason":"Invalid Age"}
        errors_list.append(err_emp)
        continue
    
    try:
        #Salary validation
        emp[headers[7]] = int(emp[headers[7]])
        if emp[headers[7]] <=0:
            err_emp = {"emp_id":emp[headers[0]],"error_reason":"Invalid Salary"}
            errors_list.append(err_emp)
            continue
    except Exception:
        err_emp = {"emp_id":emp[headers[0]],"error_reason":"Invalid Salary"}
        errors_list.append(err_emp)
        continue
    
    try:
        #phone number validation
        if len(emp[headers[8]])!=10:
            err_emp = {"emp_id":emp[headers[0]],"error_reason":"Phone Number should be 10 Digits"}
            errors_list.append(err_emp)
            continue
             
        emp[headers[8]] = int(emp[headers[8]])
            
    except Exception:
        err_emp = {"emp_id":emp[headers[0]],"error_reason":"Invalid Phone Number"}
        errors_list.append(err_emp)
        continue
    #Email Validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, emp[headers[9]]):
        err_emp = {"emp_id":emp[headers[0]],"error_reason":"Invalid Email"}
        errors_list.append(err_emp)
        continue
    
    #Department Validation      
    if emp[headers[6]]=="" or emp[headers[6]] is None:
        err_emp = {"emp_id":emp[headers[0]],"error_reason":"Invalid Department"}
        errors_list.append(err_emp)
        continue
    #Appending to cleaned_list
    cleaned_list.append(emp)
print("Error Rows :", len(errors_list))
print("Cleaned Rows",len(cleaned_list))
new_cleaned_json = {}
new_cleaned_json['cleaned_employees'] = cleaned_list
new_error_json = {}
new_error_json['errors'] = errors_list
with open('employees_errors1.json','w') as file:
    write = json.dump(new_error_json,file,indent=2)

with open('employees_cleaned1.json','w') as file:
    write = json.dump(new_cleaned_json,file,indent=2)
    
#Sample Output 
# Error Rows : 24
# Cleaned Rows 26

#employees_errors1.json
#employees_cleaned1.json
#employees_raw1.json