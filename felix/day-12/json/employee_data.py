import json

cleaned = []
errors = []

with open("employees_raw.json","r") as employee_data:
    
    employee_raw_data = json.load(employee_data)
    employee = employee_raw_data["employees"]
    required_fields = list(employee[0].keys())
    
    for item in employee:
        flag = 0
        for key in required_fields:
            if item[key] == None or str(item[key]).strip() == "":
                flag = 1
                errors.append({"id":item[required_fields[0]],"error_reason":"Field if None"})
                break
        if flag == 1:
            continue
        
        if int(item[required_fields[2]]) <18 or item[required_fields[2]]>65:
            errors.append({"id":item[required_fields[0]],"error_reason":"age is not valid"})
            continue
        
        if len(item[required_fields[9]].split("@")) != 2:
            errors.append({"id":item[required_fields[0]],"error_reason":"email is not valid"})
            continue
        
        
        try:
            if int(item[required_fields[7]])<=0:
                errors.append({"id":item[required_fields[0]],"error_reason":"salary not valid"})
                continue
            if not int(item[required_fields[8]]):
                errors.append({"id":item[required_fields[0]],"error_reason":"phone number not valid"})
                continue
            if len(str(item[required_fields[8]]))!=10:
                errors.append({"id":item[required_fields[0]],"error_reason":"phone number not valid"})
                continue
            
        except Exception:
            errors.append({"id":item[required_fields[0]],"error_reason":"phone number not valid"})
            continue
        
        
        cleaned.append(item)
        
print("Cleaned: ",len(cleaned))
print("Error: ",len(errors))
            
with open("employee_errors.json","a") as cleaned_data:
    json.dump(errors,cleaned_data,indent=2)
    
with open("employees_cleaned.json","a") as cleaned_data:
    json.dump(cleaned,cleaned_data,indent=2)

                

