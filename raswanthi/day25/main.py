import json
from mysql_connection import load_jsondata_to_mysql, read_mysql, insert_employee
from transform_data import transform_data_func
from mongo_connection import get_collection, insert_many, mongo_crud

def main():
    # # Step 1: Read JSON file
    # with open("employees.json", "r") as file:
    #     employees_data = json.load(file)

    # # Step 2: Load JSON → MySQL
    # load_jsondata_to_mysql(employees_data)   

    # Step 3: Read from MySQL → Python
    employees = read_mysql()
    print("Employees from MySQL:", employees)

    # # Step 4: Insert one extra employee
    # insert_employee(
    #     emp_id=211,
    #     name="Tara Jeff",
    #     department="Cloud",
    #     age=26,
    #     city="Hyderabad"
    # )

    # Step 5: Transform Data
    transformed_datas = transform_data_func(employees)
    print("Transformed Employees:", transformed_datas)

    # Step 6: Store into MongoDB
    emp_collection = get_collection()
    insert_many(emp_collection, transformed_datas)

    # Step 7: Perform CRUD on MongoDB
    mongo_crud(emp_collection)

if __name__ == "__main__":
    main()
