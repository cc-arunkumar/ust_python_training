import json
from db_connection import get_mysql_connection

class MySQLService:

    def __init__(self):
        self.conn = get_mysql_connection()
        self.cursor = self.conn.cursor()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INT PRIMARY KEY,
            name VARCHAR(50),
            department VARCHAR(30),
            age INT,
            city VARCHAR(30)
        );
        """
        self.cursor.execute(query)
        self.conn.commit()
        print("MySQL Table Created (if not exists).")

    def load_json_to_mysql(self, json_file):
        with open(json_file, "r") as f:
            employees = json.load(f)

        query = """
        INSERT INTO employees (emp_id, name, department, age, city)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            department = VALUES(department),
            age = VALUES(age),
            city = VALUES(city);
        """

        for emp in employees:
            self.cursor.execute(query, (
                emp["emp_id"], emp["name"], emp["department"],
                emp["age"], emp["city"]
            ))

        self.conn.commit()
        print("JSON Data Inserted Into MySQL Successfully.")

    def read_employees(self):
        self.cursor.execute("SELECT * FROM employees")
        rows = self.cursor.fetchall()
        print("Data Read From MySQL:", rows)
        return rows
