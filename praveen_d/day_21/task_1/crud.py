import pymysql
def get_connection():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
    )
    return conn

def create_employee(employee_details):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        print("connection")
        
        query="""
        INSERT INTO ust_db.emp_ust_db(first_name,last_name,
        email,position,
        salary,hire_date
        )
        VALUES(
            %s,%s,
            %s,%s,
            %s,%s
        )
        """
        values=(
            employee_details.first_name,employee_details.last_name,
            employee_details.email,employee_details.position,
            employee_details.salary,employee_details.hire_date
        )    
        
        cursor.execute(query,values)
        conn.commit()
        print("Employee created sucessfully")
        return {"message":"Created sucessfully"}
    
    except Exception as e:
        print("Employee_creation:",e)
    finally:
        cursor.close()
        conn.close()
        
# GET /employees/{employee_id} - Get employee details by ID.
# URL Parameter: employee_id
# Response: Employee details.

def get_employee():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        # print("connection")
        
        query="""
                SELECT * FROM ust_db.emp_ust_db
        """
        
        cursor.execute(query)
        result=cursor.fetchall()
        conn.commit()
        return {result}
    
    except Exception as e:
        print("Employee_creation:",e)
    finally:
        cursor.close()
        conn.close()
        
def update_employee(employee_details,emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        query="""
        UPDATE ust_db.emp_ust_db 
        SET first_name=%s,
        last_name=%s,
        email=%s,
        position=%s,
        salary=%s,
        hire_date=%s
        WHERE employee_id=%s
        """
    
        values=(
            employee_details.first_name,employee_details.last_name,
            employee_details.email,employee_details.position,
            employee_details.salary,employee_details.hire_date,emp_id
        )    
        
        cursor.execute(query,values)
        conn.commit()
        print("Employee updated sucessfully")
        return employee_details
    
    except Exception as e:
        print("Employee_creation:",e)
    finally:
        cursor.close()
        conn.close()
        
 
# . DELETE /employees/{employee_id} - Delete an employee.
# URL Parameter: employee_id
# Response: Success or failure message.

       
def delete_employee(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        query="""
        DELETE FROM ust_db.emp_ust_db 
        WHERE employee_id=%s
        """   
        
        cursor.execute(query,(emp_id,))
        conn.commit()
        print("Employee updated sucessfully")
        return "employee_deleted"
    
    except Exception as e:
        print("Employee_creation:",e)
    finally:
        cursor.close()
        conn.close()