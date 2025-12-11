import json
import pymysql
import mysql_connection
import mongo_connection

# 1
def load_json_to_mysql():
    with open("employees.json", "r") as f:
        employees = json.load(f)

    conn = mysql_connection.get_mysql_connection()
    cursor = conn.cursor()

    for emp in employees:
        try:
            cursor.execute(
                "INSERT INTO employees (emp_id, name, department, age, city) VALUES (%s, %s, %s, %s, %s)",
                (emp["emp_id"], emp["name"], emp["department"], emp["age"], emp["city"])
            )
        except pymysql.err.IntegrityError:
            print(f"Duplicate emp_id {emp['emp_id']} skipped.")

    conn.commit()
    cursor.execute("SELECT COUNT(*) AS count FROM employees")
    print("Row count in MySQL:", cursor.fetchone()["count"])
    conn.close()

#2
def read_mysql_data():
    conn = mysql_connection.get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    print("Employees from MySQL:", rows)
    return rows

#3
def transform_data(rows):
    for emp in rows:
        emp["category"] = "Fresher" if emp["age"] < 25 else "Experienced"
    print("Transformed Data:", rows)
    return rows

#4
def store_in_mongo(data):
    db = mongo_connection.get_mongo_connection()
    collection = db["employees"]
    collection.delete_many({})  # clear existing
    collection.insert_many(data)
    print("Inserted into MongoDB.")

#5
def mongo_crud():
    db = mongo_connection.get_mongo_connection()
    collection = db["employees"]

    # Insert ONE
    collection.insert_one({"emp_id": 300, "name": "New Employee", "department": "HR"})
    print("Inserted one new employee.")

    # Read ALL
    for doc in collection.find():
        print(doc)

    # Update ONE
    collection.update_one({"emp_id": 202}, {"$set": {"city": "Mumbai", "department": "DevOps"}})
    print("Updated employee 202.")

    # Delete ONE
    collection.delete_one({"emp_id": 203})
    print("Deleted employee 203.")

    # Delete MANY
    collection.delete_many({"department": "Testing"})
    print("Deleted all Testing employees.")

# --- Main Execution ---
if __name__ == "__main__":
    load_json_to_mysql()
    rows = read_mysql_data()
    transformed = transform_data(rows)
    store_in_mongo(transformed)
    mongo_crud()