import pymysql

# -----------------------------
# Database connection function
# -----------------------------
def get_connection():
    """
    Establish and return a connection to the MySQL database.
    - host: the server where MySQL is running (localhost if on same machine)
    - user: MySQL username
    - password: MySQL password
    - database: the specific DB you want to connect to
    - cursorclass: DictCursor returns rows as dictionaries (column names as keys)
    """
    return pymysql.connect(
        host="localhost",                 # MySQL server host
        user="root",                      # MySQL username
        password="pass@word1",            # MySQL password
        database="ust_asset_db",          # Database name
    )
