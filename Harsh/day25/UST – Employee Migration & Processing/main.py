from json_dump_to_mysql import load_json_to_mysql
from mysql_read import read_employees_from_mysql
from mongo_load import insert_into_mongodb
from mongo_crud import mongo_crud_operations

if __name__ == "__main__":
    print("\n=== Pipeline Start ===")

    load_json_to_mysql()
    employees = read_employees_from_mysql()
    insert_into_mongodb(employees)   
    mongo_crud_operations()

    print("=== Pipeline Complete ===\n")
