import json
import re

path = "C:/Users/303391/Desktop/ust_python_training/arjun_j_s/day_12/task2/"

def clean_name(name):
    name_split = name.split()
    new_name=""
    for i in name_split:
        new_name+=i+" "
    return new_name.strip()

def validate(item,req):
    try:
        for data in item:
            if data in req:
                if(len(str(item[data]).strip())==0 or item[data]==None):
                    return False,"No valid value"
                else:
                    if data==req[2] and int(item[req[2]]):
                        if int(item[req[2]])>65 or int(item[req[2]])<18:
                            return False,"Not a valid age for employee"
                    if data==req[7] and int(item[req[7]])<0:
                        return False,"Not valid salary"
                    if data==req[8] and int(item[req[8]]) and len(str(item[req[8]]))!=10:
                        return False,"Not a valid phone number"
                    if data==req[9] and  len(item[req[9]].split("@"))!=2:
                        return False,"Not a valid email"

            else:
                return False,"Field Missing"
    except Exception as e:
        return False,str(e)
    else:
        return True,"Success"





with open(path+"employees_raw.json","r") as employee_data_file:

    emp_data = json.load(employee_data_file)
    emp_cleaned = []
    emp_skipped = []
    req = list(emp_data["employees"][0].keys())
    
    for data in emp_data["employees"]:
        condition,stmt = validate(data,req)
        if(condition):
            data[req[1]] = clean_name(data[req[1]])
            emp_cleaned.append(data)
        else:
            emp_skipped.append({data[req[0]] : stmt})


with open(path+"employees_cleaned.json","w") as employee_data_file:
    json.dump(emp_cleaned,employee_data_file,indent=2)

with open(path+"employees_error.json","w") as employee_data_file:
    json.dump(emp_skipped,employee_data_file,indent=2)
print("Total records",len(emp_data["employees"]))
print("Total cleaned",len(emp_cleaned))
print("Total skipped",len(emp_skipped))

                
                
                