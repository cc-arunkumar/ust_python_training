


# 5. Store the transformed data into MongoDB (ust_mongo_db)
# 6. Perform basic CRUD operations in both MySQL and MongoDB

import json
from sql_dummping import dump_data,read_sql_db,modify_data
from dump_into_json import dump_data_to_json

sql_data_dict={}
# 1. Read JSON sample employee data
def read_json():
    with open("employee.json","r") as file:
        employee_data=json.load(file)
        print(employee_data)
        
        # 2. Load it into MySQL (ust_mysql_db)
        result=dump_data(employee_data)

# 3. Read data back from MySQL using Python
def read_form_sql_db():
    sql_data_dict=read_sql_db()
    print("Read sucessfully")
    return sql_data_dict

# 4. Modify/transform the data slightly
def modify_sql_data():
    result=modify_data(read_form_sql_db())
    print("Modified Sucessfully")
    return result

def dump_json():
    # print(modify_sql_data())
    result=dump_data_to_json(modify_sql_data())
    print(result)

 
def crud_operations():
    while True:
        print("1.Read json:")
        print("2.Read From sql_DB:")
        print("3.Modify sql_data:")
        print("4.Dump JSON:")
        print("5.Exit")
        option=int(input("Enter the option:"))
        match option:
            case 1:
                read_json()
            case 2:
                read_form_sql_db()
            case 3:
                modify_sql_data()
            case 4:
                dump_json()
            case 5:
                print("Exiting.................")
                break
                                
    

    
if __name__=="__main__":
    crud_operations()
    
    