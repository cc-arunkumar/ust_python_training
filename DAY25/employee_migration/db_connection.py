import pymysql

def get_db_connection():
    try:
        conn=pymysql.connect(
            host="localhost",
            user="root",
            password="pass@word1",
            database="ust_mysql_db"            
        )
        return conn
    
    except Exception as e:
        return ("DB connection Failed :",e)