from json_to_sqldb import read_json,import_to_sqldb
from sqldb_to_python import read_records_from_db
from modify_data_python import modify_data
from data_to_mongo import insert_all_data_mongo
from mongo_crud import read_all,delete_employee,delete_employees,update_record,insert_one
#read data from json and import in sql db
# data = read_json()
# try:
#     for row in data:
#         if import_to_sqldb(row):
#             print("Row Inserted Successfully")

# except Exception as e:
#     print(f"{e}")
    
#Read data from sqldb and print it as python Dictionary Format 
# data = read_records_from_db()
# for emp in data:
#     print(emp)
    
#modify the data to add a column
data = read_records_from_db()
updated_data = []
for emp in data:
    emp = modify_data(emp)
    updated_data.append(emp)
    # print(emp)
    
#inserting all data from modified dictionary to mongo
# result = insert_all_data_mongo(updated_data)
# print(result)

# print(insert_one({
#  "emp_id": 206,
#  "name": "Ajith Kumar",
#  "department": "AIML",
#  "age": 36,
#  "city": "Bangalore",
#  "category" : "Experienced"
#  }))


# print(delete_employee(206))

# print(delete_employees("AIML"))