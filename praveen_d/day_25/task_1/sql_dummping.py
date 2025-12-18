import pymysql


def get_connection():
    conn =pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
    )
    return conn

def dump_data(emp_data):
    print("hi")
    conn=get_connection()
    cursor=conn.cursor()
    try:
        for emp in emp_data: 
            # print(emp.emp_id)  
            query="""
                INSERT INTO ust_db.emp_mig(emp_id,name,department,age,city) 
                VALUES (%s,%s,%s,%s,%s)
            """
            values=(emp["emp_id"],emp["name"],emp["department"],emp["age"],emp["city"])
            cursor.execute(query,values)
        conn.commit()
        return "Successfully dumped the data into sql"
    except Exception as e:
        print("Exception in sql dummping:",e)
    finally:
        cursor.close()
        conn.close()
        

def read_sql_db():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """
            SELECT * FROM ust_db.emp_mig
        """
        cursor.execute(query)
        result = cursor.fetchall()
        
        # Get column names
        columns = []
        for desc in cursor.description:
            columns.append(desc[0])
        
        # Convert result into a list of dictionaries
        result_dict = []
        for row in result:
            row_dict = dict(zip(columns, row))  # Create dictionary for each row
            result_dict.append(row_dict)
        
        return result_dict
    
    except Exception as e:
        print("Exception from SQL reading:", e)
    finally:
        cursor.close()
        conn.close()
        
def modify_data(emp_data):
    for emp in emp_data:
        if emp["age"]<25:
            emp["category"]="Fresher"
        else:
            emp["category"]="Experienced"
    return emp_data


   