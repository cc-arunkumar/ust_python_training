import pymongo
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
from modify_data import modify_data  # Import modify_data function
import pymysql

def store_to_mongo():
    # Step 1: Connect to MySQL to read the data
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

    cursor = conn.cursor()

    # Read all employee rows from MySQL
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    # Convert to Python dictionaries
    employees_data = []
    for emp in employees:
        employees_data.append({
            "emp_id": emp[0],
            "name": emp[1],
            "department": emp[2],
            "age": emp[3],
            "city": emp[4]
        })

    # Modify the data (add category field)
    modified_employees = modify_data(employees_data)

    # Step 2: Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
    db = client['ust_mongo_db']  # Use the 'ust_mongo_db' database
    collection = db['employees']  # Use the 'employees' collection

    # Step 3: Clear existing collection (if any) before inserting new data
    collection.delete_many({})

    # Step 4: Insert the modified employee data into MongoDB
    collection.insert_many(modified_employees)
    
    print("Data successfully inserted into MongoDB.")

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Call the function to store data in MongoDB
store_to_mongo()

# Data successfully inserted into MongoDB.