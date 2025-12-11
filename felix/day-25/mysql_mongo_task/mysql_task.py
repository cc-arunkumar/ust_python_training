import pymysql
import json

def get_connection():
    conn = pymysql.connect(
        host="localhost",      
        user="root",           
        password="felix_123",
        database="ust_mysql_db",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def read_json():
    with open("employees.json","r") as file:
        data = json.load(file)
        return data
            
def inset_into_mysql():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            insert into ust_mysql_db.employees values(
                %s,%s,%s,%s,%s
            )
        """        
        data = read_json()
        for emp in data:
            cursor.execute(query,tuple(emp.values()))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Data inserted to mysql")
        

def read_from_mysql():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            select * from ust_mysql_db.employees 
        """        
        cursor.execute(query)
        data = cursor.fetchall()
        for emp in data:
            print(emp)
            if emp["age"]<25:
                emp["category"] = "Fresher"
            else:
                emp["category"] = "Experienced"
        return data
    except Exception as e:
        print(e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Data inserted to mysql")





# inset_into_mysql()
read_from_mysql()
