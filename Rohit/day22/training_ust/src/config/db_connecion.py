import pymysql



def get_connection():
    return pymysql.connect(
        host="localhost",       # Database server is running locally
        user="root",            # MySQL username
        password="pass@word1",  # MySQL password
        database="ust_db_employee", # Target database name
        cursorclass=pymysql.cursors.DictCursor
    )
    

