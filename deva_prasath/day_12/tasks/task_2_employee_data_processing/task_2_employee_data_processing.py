#  UST INDIA – Employee Data Processing 
# Task 
# Scenario
#  UST HR India collects employee data from different offices:
#  Trivandrum
#  Kochi
#  Bangalore
#  Chennai
#  Pune
#  Hyderabad
#  The raw data is stored in a 
# However, the data:
#  contains missing fields
#  contains invalid salaries
#  employees_raw.json file.
#  contains wrong phone formats
#  contains extra spaces
#  contains mixed languages Indian names)
#  contains multiple religions, genders, regions
#  contains employees from all over India
#  Your task:
#   Read the raw JSON
#   Validate & clean the data
#  JSON
#  Generate a new clean JSON file 
# employees_cleaned.json
#   Generate an error file 
# employees_errors.json

import json
#opening the input file
with open(r'D:\training\ust_python_training\deva_prasath\day_12\employees_raw.json','r') as f1:
    emp=json.load(f1)

#handling various custome exceptions
class MissingRequiredField(Exception):
    pass  

#age validation
class AgeValidation(Exception):
    pass

#salary validation
class SalaryValidation(Exception):
    pass

#phone validation
class PhoneValidation(Exception):
    pass

#email validation
class EmailValidation(Exception):
    pass

#department validation
class DepartmentValidation(Exception):
    pass

#exracting list 
data=emp['employees']

#lists for errors and processed
errors=[]
processed=[]

# required_fields=["emp_id","name","age","salary","department","phone","email"]
required_fields=list(data[0].keys())

#looping through the list
for i in range(len(data)):
    try:
        #first column
        row=data[i]
        
        #checking required fields
        for j in required_fields:
            if j not in row or row.get(j) is None:
                raise MissingRequiredField(f"Data {j} is missing")
        
        #age validaition
        if not isinstance(row.get('age'),int)or not 18 <=row.get('age')<=65:
            raise AgeValidation("Invalid age")
        
        #salary validation
        try:
            sal=int(row.get('salary'))
            if sal<=0:
                raise SalaryValidation("Salary must be a positive integer")
        except ValueError:
            raise SalaryValidation("Salary is not a valid number")
        
        #phone validation
        ph=row.get('phone')
        if not ph.isdigit() or len(ph)!=10:
            raise PhoneValidation("Invalid phone number")
        
        #email validation
        if '@' not in row.get('email'):
            raise EmailValidation("Invalid email ID")

        #departmnet validation
        if not row.get('department'):
            raise DepartmentValidation("Invalid department")
        
        #manipulating name 
        if row.get('name'):
            a=row['name']
            cleaned=" ".join(a.split())
            row['name']=cleaned
            
    except (MissingRequiredField,AgeValidation,SalaryValidation,PhoneValidation,EmailValidation,DepartmentValidation) as e:
        errors.append({"emp_id":row.get('emp_id'),"error_reason":str(e)})

    else:
        #processed list appending data
        processed.append(row)

#summary printing
print("Processed Employees:", len(processed))
print("Errors Found:", len(errors))

#writing in a json file
with open('employees_cleaned.json','w') as f1:
    json.dump({'cleaned_employees':processed},f1,indent=2)

#writing in a json file
with open('employees_errors.json','w') as f2:
    json.dump({'errors':errors},f2,indent=2)

