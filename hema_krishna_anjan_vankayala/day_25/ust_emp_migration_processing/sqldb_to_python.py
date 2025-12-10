from db_connection import get_connection 


def read_records_from_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT * FROM ust_mysql_db.employees
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows 
    except Exception as e:
        return f'Error: {e}'
    
    finally:
        if conn.open:
            conn.close()
            

    