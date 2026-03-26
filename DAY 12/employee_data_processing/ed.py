import json

# Lists to store cleaned and error records
cleaned=[]
errors=[]
invalid_records=0
valid_records=0

# Load raw employee data from JSON file
with open("DAY 12\\employee_data_processing\\employees_raw.json","r") as raw_file:
    data=json.load(raw_file)

# Dynamically get required fields from first employee record
required_fields=list(data["employees"][0])

# Iterate through each employee record
for emp in data["employees"]:
    missed=[]
    flag=True

    # Check for missing or empty required fields
    for field in required_fields:
        if field not in emp or emp[field]=="" or emp[field] is None:
            missed.append(field)

    # If any required field is missing, mark as error
    if missed:
        flag=False
        errors.append(
            {
                "employee":emp.get("emp_id","UNKNOWN"),
                "error_reason":"Missing Required fields "+",".join(missed)
            }
        )        

    # Salary Validation: must be numeric and positive
    sal=emp.get("salary","")
    try:
        sal=int(sal)
        if sal<=0:
            flag=False
            errors.append({
                 "employee":emp.get("emp_id","UNKNOWN"),
                 "error_reason":"Salary must be positive"
            })
        else: emp["salary"]=sal
    except:
        flag = False
        errors.append({
            "employee":emp.get("emp_id","UNKNOWN"),
            "error_reason":"Salary is not a Number"
        })       

    # Age Validation: must be integer and between 18–65
    if type(emp.get("age"))!=int or emp["age"]<18 or emp["age"]>65:
            flag=False
            errors.append(
                {
                "employee":emp.get("emp_id","UNKNOWN"),
                "error_reason":"Invalid Age"
                }
            )

    # Department Validation: cannot be empty or None
    if type(emp.get("department")) != str or emp["department"] is None or emp["department"].strip()=="":
         flag=False
         errors.append(
              {
                   "employee":emp.get("emp_id","UNKNOWN"),
                   "error_reason":"Department name is not valid"
              }
         )

    # Name Cleaning: remove extra spaces
    emp["name"]=" ".join(emp["name"].split())

    # Email Validation: must contain '@' and not start/end with '@'
    email=emp.get("email","")
    if "@" not in email or email.startswith("@") or email.endswith("@"):
         flag=False
         errors.append({
              "employee":emp.get("emp_id","UNKNOWN"),
              "error_reason":"Email Id is not Valid"
         })
        
    # Phone number Validation: must be 10 digits and numeric
    ph_num=str(emp.get("phone",""))
    if not ph_num.isdigit() or len(ph_num)!=10:
         flag=False
         errors.append({
              "employee":emp.get("emp_id","UNKNOWN"),
              "error_reason":"Phone number invalid"
         })

    # Final Check: if all validations pass, add to cleaned list
    if flag==True:
        cleaned.append(emp)
        valid_records+=1
    else : invalid_records+=1
    

# Write cleaned employees to JSON file
with open("DAY 12\\employee_data_processing\\employees_cleaned.json","w") as cf:
    json.dump({"employees": cleaned}, cf,indent=2)

# Write error records to JSON file
with open("DAY 12\\employee_data_processing\\employees_errors.json","w") as ef:
    json.dump({"errors": errors},ef,indent=2)

# Print summary of records
print(f"Total Records :{valid_records+invalid_records}")
print(f"Valid Records :{valid_records}")
print(f"Invalid Records :{invalid_records}")


"""
SAMPLE OUTPUT

Total Records :50
Valid Records :26
Invalid Records :24
"""