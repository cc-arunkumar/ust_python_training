from json_sql import load_mysql
from mysql_mongo import data_from_sql,alter_employee_data,push_data_to_mongo


try:
    load_mysql()
    data_from_sql()
    alter_employee_data()
    push_data_to_mongo()
except Exception as e:
    print("Error in main file!")