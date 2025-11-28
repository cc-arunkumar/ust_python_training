import csv
import pymysql
from datetime import datetime

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )

def main():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO employee_directory (
        emp_code, full_name, email,
        phone, department, location, join_date, status
    ) VALUES (
        %s, %s, %s, %s, %s,
        %s, %s, %s
    )
    """

    csv_path = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\valid_employee.csv"

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                join_date = datetime.strptime(row["join_date"], "%m/%d/%Y").strftime("%Y-%m-%d")
            except ValueError:
                print(f"Skipping row due to invalid date: {row['join_date']}")
                continue  # s

            data = (
                row["emp_code"],
                row["full_name"],
                row["email"],
                row["phone"],
                row["department"],
                row["location"],
                join_date,
                row["status"],
            )

            try:
                cursor.execute(query, data)
            except Exception as e:
                print(f"Error inserting row {row}: {e}")
                continue

    conn.commit()
    cursor.close()
    conn.close()

    print("All valid CSV records inserted successfully!")

if __name__ == "__main__":
    main()
