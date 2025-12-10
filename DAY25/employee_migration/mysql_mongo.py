import pymysql
from pymongo import MongoClient
from db_connection import get_db_connection


def data_from_sql():
    try:
        conn=get_db_connection()
        cursor=conn.cursor(pymysql.cursors.DictCursor)  
        cursor.execute("SELECT * FROM employees")
        ans=cursor.fetchall()
        return ans        
    
    except Exception as e:
        print("Error in connecting MYSQL DB while reading :", e)
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            print("SQL DB connection closed")


def alter_employee_data():
    try:
        data=data_from_sql()
        for i in data:
            if i["age"]<25:
                i["category"]="Fresher"
            elif i["age"]>=25:
                i["category"]="Experienced"
        
        return data
    except Exception as e:
        print("Error in Altering Data ->", e)
       


def push_data_to_mongo():
    try:
        altered_data=alter_employee_data()
        client=MongoClient("mongodb://localhost:27017/")
        db = client["ust_mongo_db"]
        collection = db.employees

        if altered_data:
            collection.insert_many(altered_data) 
            print(f"Inserted {len(altered_data)} records into MongoDB.")
    
    except Exception as e:
        print("Error in Pushing  to MongoDB ->", e)

    finally:
        client.close()
        print("MongoDB connection closed")


       
        