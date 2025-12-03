import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_assets"
    )

def create_task(emp_id,emp_code,full_name,email,phone,
                department,location,join_date):
    
    conn = get_connection()
    cursor=conn.cursor()
    sql = """
        INSERT INTO employee_directory(
            emp_id,emp_code,full_name,email,phone,
                department,location,join_date
        )
        VALUES(
            %s,%s,%s,%s,
            %s,%s,%s,%s
        )
    """
    values = (emp_id,emp_code,full_name,email,phone,
                department,location,join_date)
    cursor.execute(sql,values)
    conn.commit()
    cursor.close()
    conn.close()
    
    print("Employee record created successfully")
    
create_task(
    emp_id=1,
    emp_code="EMP001",
    full_name="John Doe",
    email="john.doe@example.com",
    phone="9876543210",
    department="IT",
    location="Hyderabad",
    join_date="2023-05-15"

    
)