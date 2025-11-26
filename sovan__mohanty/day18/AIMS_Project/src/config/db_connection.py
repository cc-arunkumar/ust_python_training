import pymysql
def get_connection():
    # Establish connection to MySQL database
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )
    return conn # Return connection object