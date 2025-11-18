import json

class InvalidRequiredField(Exception):
    pass
class InvalidAge(Exception):
    pass
class InvalidPhoneNumber(Exception):
    pass
class InvalidEmail(Exception):
    pass
class InvalidSalary(Exception):
    pass

# required_fields = ["emp_id", "name", "age", "salary", "department", "phone", "email"]
# required_fields=list(data[0].keys())
errors = []
processed=[]
with open("C:/Users/Administrator/Desktop/sunku_sai_yaswanth/day12/task_json/employees_raw.json", 'r') as employee_processing:
    read = json.load(employee_processing)
    data = read["employees"]
    header=list(data[0].keys())

    for row in data:
        try:
            if "name" in row:
                name=row[header[1]]
                cleaned=" ".join(name.split())
                row[header[1]]==cleaned
                
            for field in header:

                if field not in row or row[field] is None or str(row[field]).strip() == "":
                    raise InvalidRequiredField(f"Field '{field}' is missing for employee")
                if "age" in row:
                    age = row[header[2]]
                    if age is None or (isinstance(age, str) and not age.isdigit()) or (int(age) < 18 or int(age) > 65):
                        raise InvalidAge(f"Invalid age {age} for employee {row.get('emp_id')}. ")
                    age = int(age)
                try:
                    sal=int(row.get(header[7]))
                    if sal<=0:
                        raise InvalidSalary("Salary must be a positive integer")
                except ValueError:
                    raise InvalidSalary("Salary is not a valid number")
                        # raise InvalidSalary(f"Invalid salary is not valid for employee {row.get('emp_id')}. ")
                
                if "phone" in row:
                    phone=row[header[8]]
                    if not phone.isdigit() or len(phone) != 10:
                        raise InvalidPhoneNumber("Invalid phone number")
                if "email" in row:
                    email=row[header[9]]
                    if "@" not in email:
                        raise InvalidEmail(f"Invalid email {email} for employee")
                
                    
                
                
        except (InvalidRequiredField ,InvalidAge,InvalidPhoneNumber,InvalidEmail,InvalidSalary)as e:
            errors.append({"emp_id": row.get("emp_id"),"error": str(e)})
        else:
            processed.append(row)
print("Processed Employees:", len(processed))
print("Errors Found:", len(errors))

with open("employee_cleaned.json",'w')as file1:
    json.dump({'employee_cleaned':processed},file1,indent=2)
with open("employee_errors.json",'w')as file2:
    json.dump({'errors':errors},file2,indent=2)
