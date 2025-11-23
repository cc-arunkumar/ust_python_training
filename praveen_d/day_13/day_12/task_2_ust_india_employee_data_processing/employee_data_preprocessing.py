import json

required_fields_list = ["emp_id","name","age","salary","department","phone","email"]
error_list=[]


def required_fields(emp_dict):
    for field in required_fields_list:
        # print(field)
        if field not in emp_dict:
            return False

        value = emp_dict[field]
        # print(value)

        if value is None or str(value).strip() == "":
            return False
    return True

def name_cleaning(emp_dict):
    # print(emp_dict)
    # print(type(emp_dict))
        emp_name=emp_dict['name']
        clean_name=" ".join(emp_name.split())
        emp_dict['name']=clean_name

def age_validation(emp_dict):
     try:
        emp_age=int(emp_dict['age'])
        emp_dict['age']=emp_age
        if emp_dict['age']>18 and emp_dict['age']<65:
            return True
     except TypeError:
        print(f"The value should be in int formate:{emp_dict['age']}")
        return False
     except ValueError:
        print(f"The value should be in int formate{emp_dict['age']}")
        return False


# SALARY VALIDATION
def salary_validation(emp_dict):
    try:
        emp_salary=int(emp_dict['salary'])
        if emp_salary>0:
            return True
        else:
            return False
    except ValueError:
        print(f"not in a perfect formate{emp_dict['salary']}")
        return False

def phone_number_validation(emp_dict):
    try:
        emp_phone_number=int(emp_dict['phone'])
        temp=emp_phone_number
        flag=0
        while(temp>0):
            flag+=1
            temp=temp//10

        if flag==10:
            return True
        else:
            # print(f"Invalid data------------------------->{emp['phone']}")
            return False
    except ValueError:
        print(f"The formate is not proper-->{emp_dict['phone']}")

# EMAIL VALIDATION
def email_validation(emp_dict):
    email=emp_dict['email']
    if "@" not in email:
        return False
    
    username,domain= email.split("@",1) #even if we have multiple @ only 1st @ will be considerd
    if username.strip()=="" or domain.strip=="":
        return False
    return True


with open("task_2_ust_india_employee_data_processing/employee.json","r") as emp_file:
    employee_file_json = json.load(emp_file)

employees_list = employee_file_json["employees"]
# print(employees_list)
# print(type(employees_list))

print(f"Total employees found: {len(employees_list)}")

count=0
validated_list=[]
error_list=[]
for emp in employees_list:
    # print(emp)
    # print(type(emp))
    is_valid = required_fields(emp)
    is_age_valid=age_validation(emp)
    is_salary_valid=salary_validation(emp)
    is_phone_valid=phone_number_validation(emp)
    is_email_valid=email_validation(emp)
    name_cleaning(emp)
    
    if is_valid==True and is_age_valid==True and is_salary_valid==True and is_phone_valid==True and is_email_valid==True:
        validated_list.append(emp)
        count+=1
    else:
        error_list.append(emp)
        
print(f"Total no of valid employee:{count}")
print(validated_list)
output_data={"employees":validated_list}
error_data={"employess":error_list}

with open("employee_cleaned.json","w") as f:
    json.dump(output_data,f,indent=4)

with open("employees_errors.json","w") as f:
    json.dump(error_data,f,indent=4)



   