import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
    )

def read_all_employees():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM emp;")
        rows = cursor.fetchall()
        for emp in rows:
            print(f"ID {emp[0]} | NAME: {emp[1]} | Salary: {emp[2]}")
    except Exception as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()

def get_employee_by_id(emp_id):
    try:  
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM emp WHERE emp_id = %s;", (emp_id,))
        row = cursor.fetchone()
        if row:
            # print(f"ID {row[0]}")
            return row[0]
        else:
            print("No employee found with that ID")
    except Exception as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
def create_employee(name, salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO emp ( emp_name, emp_salary) VALUES (%s, %s);",
            ( name, salary)
        )
        conn.commit()
        print("Employee created successfully")
    except Exception as e:
        print("Error:", e)
    finally:
        if conn():
            cursor.close()
            conn.close()
            
            
def update_employee_by_id(e_id,new_name,new_salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE ust_db.emp SET emp_name = %s, emp_salary = %s WHERE emp_id = %s",(new_name, new_salary, e_id))

        conn.commit()
        print("EMployee recors has been updated successfully")
    except Exception as e:
        print("Exception",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("COnncetion closed successfully")
        


def delete_employee(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM emp WHERE emp_id = %s;", (emp_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Employee deleted successfully")
        else:
            print("No employee found with that ID")
    except Exception as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        
        
# read_all_employees()
# # get_employee_by_id(1001)
# print(" ")
# create_employee("Rohit", 5000)
# read_all_employees()
# update_employee_by_id(1003,"taniya","500000")
# delete_employee(1005)
# delete_employee(1006)
# delete_employee(1007)
# delete_employee(1008)
