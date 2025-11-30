import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",       
        user="root",            
        password="pass@word1", 
        database="ust_practice"
    )