import pymysql
import json
def get_Connection():
    return pymysql.connect(
        host="localhost",      # Database server host
        user="root",           # Database username
        password="password123", # Database password
        database="ust_mysql_db", # Database name
        cursorclass=pymysql.cursors.DictCursor
    )
    
headers=["emp_id","name","department","age","city"]
def dumping_into_db(emp):
    try:
        conn=get_Connection()
        cursor=conn.cursor()
        query=""" INSERT INTO EMPLOYEES (emp_id,name,department,age,city) VALUES(%s,%s,%s,%s,%s)"""
        data=(emp["emp_id"],emp["name"],emp["department"],emp["age"],emp["city"])
        cursor.execute(query,data)  
        conn.commit()
    except Exception as e:
        print("Error",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            
# with open("employees.json","r") as file:
#             content=json.load(file)
#             for row in content:
#                 dumping_into_db(row)



def reading_from_sql():
    try:
        conn=get_Connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM EMPLOYEES")
        content=cursor.fetchall()
        for row in content:
    #         print({headers[0]:row[0],headers[1]:row[1],headers[2]:row[2],headers[3]:row[3],headers[4]:row[4]})
              print(row)
    
    except Exception as e:
        print("Error",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()



def update_category():
    try:
        conn=get_Connection()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM EMPLOYEES")
        content=cursor.fetchall()
        for row in content:
            if row["age"]<25:
               row["category"]="Fresher"
            else:
                row["category"]="Experienced"
        for row in content:
            print(row)
        return content
    except Exception as e:
        print("Error",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
    


# update_category()

# reading_from_sql()


    
