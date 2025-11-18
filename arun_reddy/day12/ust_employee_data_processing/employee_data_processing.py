import json

class MissingFieldException(Exception):
    pass
class AgeValidationException(Exception):
    pass
class EmailException(Exception):
    pass

# Lists to track valid and invalid employee records
valid_employees = []
invalid_employees = []

def validate(row,required_fields):
    try:
        
        for req in row:
            if req not in required_fields:
                raise MissingFieldException
            else:
                if len(str(row[req]).strip()) == 0 or row[req]==None :
                    raise Exception
                list1=row["name"].split(" ")
                if len(list1)>2:
                    strng=""
                    for item in list1:
                        strng+=item
                        strng+=" "
                row["name"]=strng.strip()
                if int(row["age"]):
                    if int(row["age"])<18 or int(row["age"])>65:
                        raise AgeValidationException
                if int(row["salary"])<0 :
                    raise Exception
                row["salary"]=int(row["salary"])
            
                if int(row["phone"]) and len(row["phone"])!=10:
                    raise Exception
                
                eml=row["email"]
                emails=eml.split("@")
                if len(emails)!=2:
                    raise EmailException
    except MissingFieldException as mfe:
        return False,f"Missing Fields"
    except AgeValidationException as ave:
        return False,f"Age Invalid"
    except EmailException as ee:
        return False,f"Email Invalid"
    except Exception as e:
        return False,f"Invalid Details"
    else:
        return True,f"Valid"

required_fields = ["emp_id", "name", "age", "salary", "department", "phone", "email"]

with open("employees_raw.json", "r") as file:
    content = json.load(file)
    my_dict = content["employees"]
    required_fields = list(my_dict[0].keys())
    
    for row in my_dict:
        flag,mssg=validate(row,required_fields)
        if flag:
            valid_employees.append(row)
        else:
            invalid_employees.append({row["emp_id"]:mssg})
        

# Print summary
print(f"\nValid employees: {len(valid_employees)}")
print(f"Invalid employees: {len(invalid_employees)}")

        
with open("employees_errors.json","w",newline='') as file:
    json.dump(invalid_employees,file,indent=2)
with open("employees_cleaned.json","w",newline='') as file:
    json.dump(valid_employees,file,indent=2)
    
    

    