import json

def validate(row):
    required = ["emp_id","name","age","salary","department","phone","email"]
    try:
        for i in row:
            if str(row[i]).strip()=="" or row[i]==None:
                return False,"Field is empty"
            if i == required[2]:
                if (row[i]<18 or row[i]>65):
                    return False,"Invalid age"
            if i == required[3]  and int(row[i])<0:
                return False,"Invalid Salary"
            if i== required[5]  and int(row[i]):
                if len(str(row[i])) != 10:
                    return False,"Invalid Phone number"
            if i == required[6] :
                e_list = row[i].split("@")
                if len(e_list)!=2:
                    # print(f"{row["emp_id"]}")
                    return False,"Invalid email"
        return True,"validation complete"

    except Exception as e:
        return False,str(e)


error = []
cleaned = []
with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day12/ust_employee_data_processing/employees_raw.json","r") as employees_json_data:
    data = json.load(employees_json_data)
    employees = data["employees"]
    # print(employees)
    print("Total: ",len(employees))
    for row in employees:
        condition, reason = validate(row)
        if condition:
            # removing extra space in between names
            name_list = row["name"].split()
            row["name"] = " ".join(name_list)
            # appending valid to cleaned list
            cleaned.append(row)
        else:
            error.append(f"Error {row["emp_id"]}: {reason}")
    with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day12/ust_employee_data_processing/employees_cleaned.json","w") as cleaned_json_data:
        json.dump(cleaned,cleaned_json_data,indent=2)
    with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day12/ust_employee_data_processing/employees_error.json","w") as error_json_data:
        json.dump(error,error_json_data,indent=2)
    print("Total cleaned: ",len(cleaned))
    print("Total skipped: ",len(error))