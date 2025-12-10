import pymysql, json 
from db_connection import get_connection

def read_json():
    with open('employees.json','r') as file:
        reader = json.load(file)
    return reader 

def import_to_sqldb(row):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO ust_mysql_db.employees (emp_id,name,department,age,city) VALUES
        (%s,%s,%s,%s,%s)
        """
        values = (row['emp_id'],row['name'],row['department'],row['age'],row['city'])
        
        cursor.execute(query,values)
        conn.commit()
        return True
    except Exception as e:
        return f'Error:{e}'
    
    finally:
        if conn:
            conn.close()
    
