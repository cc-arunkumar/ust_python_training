import pymysql
import pymongo

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_mysql_db"
    )
def get_mongo_connection():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    return client
    
conn= get_connection()
cursor=conn.cursor(pymysql.cursors.DictCursor)
sql="SELECT * FROM employees"
cursor.execute(sql)
employees=cursor.fetchall()
cursor.close()
conn.close()

for emp in employees:
    if emp["age"]<=25:
        emp["category"] = "Fresher"
    else:
        emp["category"] = "Experienced"

client = get_mongo_connection()
db =client["ust_mongo_db"]
collection=db["employees"]

employees=collection.find()       
for emp in employees:
        new_category = "Fresher" if emp["age"] <= 25 else "Experienced"
        collection.update_one(
            {"emp_id":emp["emp_id"]},
            {"$set":{"category":new_category}}
                            )
print("category updated")

collection.insert_many(employees)

print("Transformed employees inserted into mongodb")