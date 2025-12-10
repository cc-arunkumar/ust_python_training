import json 
import pymysql

from  db_connection import get_connection

with open(r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day25\data.json", mode="r") as file1:
    data =json.load(file1)
    try:
        
        conn =  get_connection()
        cursor = conn.cursor()
        
        row= 0
        for row in data:
            query = """
            INSERT INTO employees
            (emp_id, name,  department, age, city)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (
                row["emp_id"], row["name"], row["department"], row["age"], 
                row["city"]
            )
            cursor.execute(query,values)
            conn.commit()
            row+=1
            
        print("total number of rows inserted",row)
            
            
    except Exception as e:
        raise ValueError(e)
    finally:
        if cursor: cursor.close()
        if conn: conn.close()


