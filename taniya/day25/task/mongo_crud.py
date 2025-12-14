import pymysql
import pymongo

def get_mysql_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_mysql_db"
    )

def get_mongo_connection():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    return client["ust_mongo_db"]

def mysql_to_mongo():
    conn = get_mysql_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()

    for emp in employees:
        emp["category"] = "Fresher" if emp["age"] <= 25 else "Experienced"

    db = get_mongo_connection()
    collection = db["employees"]
    collection.delete_many({})
    collection.insert_many(employees)
    # print("Employees synced from MySQL to MongoDB with category")

def update_employee_age(collection, emp_id, new_age):
    new_category = "Fresher" if new_age <= 25 else "Experienced"
    collection.update_one(
        {"emp_id": emp_id},
        {"$set": {"age": new_age, "category": new_category}}
    )
    # print(f"Updated emp_id={emp_id}: age={new_age}, category={new_category}")
def get_category(emp):
    return "Fresher" if emp["age"] <= 25 else "Experienced"
def main():
    db = get_mongo_connection()
    collection = db["employees"]

    mysql_to_mongo()

    # print("All employees in MongoDB:")
    # for emp in collection.find():
    #     print(emp)\
        
    new_employee={
        "emp_id":250,
        "name":"Amit",
        "age":35,
        "city":"hyd"
    }
    new_employee["category"]=get_category(new_employee)
    collection.insert_one(new_employee)
    

    update_employee_age(collection, 250, 26)

    # print("Remaining employees after update:")
    total = 0
    for emp in collection.find():
        total += 1
    counter = 0
    for emp in collection.find({"age":{"$lte":22}}):
        counter += 1
    print(f"Total = {total}, Found = {counter}")
    count = 0
    for emp in collection.find({"category":"Fresher"}):
        count += 1
    print(f"Total = {total},freshers = {count}")
if __name__ == "__main__":
    main()
    
    
